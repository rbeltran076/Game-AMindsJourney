# Making the games with and without graphics
from graphics import *
from objects import *
from windows import *
from functions import *
import time

# Run game In terminal
def run_game_in_terminal():
    # Create an object player
    player = Player(
        inventory = [],
        orientation = "north",
        position = "start"
    )
    print(f"\n\nWelcome to A Mind's Journey!\n(The 'run on terminal' version...)")
    print(get_data("room", player.position, "description"))

    command = input("Enter a command\n(press h to see commands available) >> ").lower()

    gameOver = False
    while gameOver == False:
        # set the score counter.
        # Each time the puzzle is opened, the score increases 
        # score =+ 1
        score = 0
        # Start the display
        print("__________________________________________________")

        # Do not continue until receiving something in the input space
        while not command:
            print(f"\n\nEnter a command...\n")
            command = input("Enter a command\n(press h to see commands available) >> ").lower().split(" ")
            
        if command[0] == "look":
            player.orientation = command[1]
            print()
            print(f"You look {player.orientation}\n")
            print(get_data("room", player.position, player.orientation))
            print("\n\n")

        elif command[0] == "move":
            # Define the direction as the second word from the command
            direction = command[1]

            # Tell the player it has moved
            print()
            print(f"You move {direction}")

            # call the move() function to tell if the player can move
            move(player, direction)

            # print the description of the room the player is in
            print()
            print(f"You are in the {get_data('room', player.position, 'name')}")
            print(get_data("room", player.position, "description"))
            
        elif command[0] == "get":
            item = command[1]
            get(player, player.inventory, item)

        elif command[0] == "inventory":
            # show the inventory
            print("\nYou check your inventory...")
            print(player.inventory)

            # If the inventory is empty tell the player
            if len(player.inventory) == 0:
                print("You don't have anything in your inventory")
        
        elif command[0] == "h":
            print_help()

        else:
            print("\n((!!!)) Invalid command ((!!!))\n")
            print_help()

        # Print the elements in the room
        print(f"\nThe elements that you can find in this room are:\n{get_data('room', player.position, 'elements')}\n")

        if get_data('room', player.position, 'item') not in player.inventory:
            # Print the items that are in the room
            print(f"\nThe item that you can find in this room is:\n{get_data('item', player.position, 'name')}")
            print(f"{get_data('item', player.position, 'description')}\n")
        else:
            print("You already collected the items here")

        if player.position == "puzzle":
            puzzleAnswer = input("\nDo you want to solve the puzzle? (y/n)\n").lower()
            if puzzleAnswer == "y":
                puzzle(player, player.inventory, score)
            else:
                pass
        
        # if the game has not finished...
        if not gameOver:
            # Ask for a command again
            command = input("\nEnter a command\n(press h to see commands available) >> ").lower().split(' ')
# run_game_in_terminal()

# With graphics
def run_game_with_graphics():
    # define the score. The larger, the worse
    # increases each time the puzzle is attempted
    score = 0

    # Show the menu
    Menu()

    # Initialize the player facing 
    # north in the start roomasdasdasd
    player = Player(
        inventory = [],         # Empty inventory
        orientation = "north",  # Facing north
        position = "start"      # Start room
        )

    # After the "startButton" is pressed
    startInterface = Interface(player.position, player.inventory, isPuzzle=False, score = score) 
    player.reposition(startInterface.getRoom())
    
    gameOver = False
    while gameOver == False:
        newInterface = Interface(player.position, player.inventory, isPuzzle=False, score = score) 
        player.reposition(newInterface.getRoom())

        # if the player is in the puzzle room...
        if player.position == "puzzle":
            puzzleInterface = Interface(player.position, player.inventory, isPuzzle=True, score = score)
            player.reposition(puzzleInterface.getRoom())
# run_game_with_graphics()