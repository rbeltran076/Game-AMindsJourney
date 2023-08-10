# The programming final project
# made by Ronald Beltran

from graphics import *
from windows import *
from objects import *
from games import *
from functions import *

# Create objects
# rooms, items = create_objects()
def main():
    # Introduction and prompt for the player
    print("\n\nHello, welcome to A mind's Journey,\na text-based game developed in Python by Ronald Beltran.")
    print("Would you like to play (in the Terminal) or (with Graphics)? (0 / 1)")

    # Continuously ask for input until a valid answer is given
    while True:
        # Get the player's choice
        answer = input()

        # If the player chose terminal mode
        if answer == '0':
            # Run the game in terminal mode
            run_game_in_terminal()
        # If the player chose graphics mode
        elif answer == '1':
            # Run the game in graphics mode
            run_game_with_graphics()
        else:
            # If the player's input is invalid, ask again
            print("\nPlease enter 0 or 1.\n")

# Call the main function to start the game
main()
