# Useful functions for using in the rest of the scripts
import json
import time
from Button import Button
from graphics import *
from objects import *

# Function that retrieves data from the .json
# file and returns its value
def get_data(className, instance, feature):
    if className == "room" or className == "item":
        # className could be only "room" or "item"
        filepath = "gameFinalProject/data/" + className + "-features.json"
        with open(filepath, "r") as file:
            data = json.load(file)
            if data != KeyError:
                return data[instance + "-room"][feature]
            else:
                return f"{data[instance + '-room'][feature]}"
    else:
        raise NameError("Enter either 'room' or 'item' as className")

# print command guide
def print_help():
    print("Commands available:")
    print("\tlook [north, south, ease, west, up, down]")
    print("\tmove [north, south, east, west]")
    print("\tget <item>")
    print("\tinventory")
    print("\texit")
    print()

# A function that decides if the player can move in
# a certain direction or not.
def move(player, direction):
    # Define room names and exits
    rooms = {
        "start": {"north": "curiosity"},
        "curiosity": {"north": "puzzle", "east": "acceptance"},
        "acceptance": {"east": "knowledge", "west": "curiosity"},
        "knowledge": {"north": "communication", "west": "acceptance"},
        "communication": {"south": "knowledge", "west": "love"},
        "love": {"east": "communication", "west": "puzzle"},
        "puzzle": {"south": "curiosity"}
    }

    # if the command's direction is a direction of an exit..
    if direction in rooms[player.position]:

        # set the player position to the second word of the command
        player.position = rooms[player.position][direction]
        
        # Define the new position
        print(f"You are now in the {player.position} room...")

    else:
        print(f"You can't go {direction}")

# a function that appends the item in the player.inventory
# list if it is not in it.
# Else, prints that the player already has the item
def get(player, inventory, item):
    # Define the valid items to collect
    items = [
        "curiosity",
        "acceptance",
        "knowledge",
        "communication",
        "love"
        ]
    
    # if the item exists and it is in the room
    if item in items and player.position == item:
        # if the item is not in the inventory...
        if item not in player.inventory:
            # Add item to player.inventory
            player.inventory.append(item)
        else:
            print(f"You already have {item}!")
    
    # if the item exists but it is not in that room
    elif item in items and player.position != item:
        print(f"You cannot find {item} in this room.. maybe another one")
    
    # if the item doesn't exist
    else:
        print(f"hahah no... '{item}' is not an item you can get")
        print(f"The items you can get are: {items}")

# same function but for graphics version
def get_with_graphs(inventory, item):
    # Define the valid items to collect
    items = [
        "curiosity",
        "acceptance",
        "knowledge",
        "communication",
        "love"
        ]
    
    # Since the logic is already in the interface object.
    # Just append the item.
    if item in items:
        return inventory.append(item)
        
# ================= Thi function is never used in the game code. Take it as an unreleased feature. 
# This is the first prototype of the puzzle (it was too complex to do properly in the time I had)
def puzzle_with_graphs0(inventory, score):
    if len(inventory) == 5:
        # increase score =+ 1
        score += 1

        # declare the inventory the puzzle is going to work with
        puzzleWin = GraphWin("Final Puzzle", 500, 500)
        puzzleWin.setCoords(-250, -250, 250, 250)
        puzzleWin.setBackground('white')

        itemBoxCoords = [
            (-100, 200),
            (-50, 200),
            (0, 200),
            (50, 200),
            (100, 200)
            ]
        
        puzzleBoxCoords = [
            (0, 150),       # Head
            (0, 0),         # Chest
            (150, 0),       # Left Arm
            (-150, 0),      # Right Arm
            (0, -150)       # Legs
        ]
        
        buttonParams = {
            # Buttons for the item bar
            "curiosity":        (-100, 200, "take"),
            "acceptance":       (-50, 200, "take"),
            "knowledge":        (0, 200, "take"),
            "communication":    (50, 200, "take"),
            "love":             (100, 200, "take"),

            # Buttons for the puzzle boxes
            "curiosityBox":     (0, 150, "place"),       
            "acceptanceBox":    (0, 0, "place"),         
            "knowledgeBox":     (150, 0, "place"),        
            "communicationBox": (-150, 0, "place"),       
            "loveBox":          (0, -150, "place"),

            # Button to submit answer to puzzle   
            "enterButton":          (-200, -200, "Enter")       
        }
    
        # Draw head
        head = Circle(Point(0, 100), 50)
        head.setFill("black")
        head.draw(puzzleWin)

        # Draw body
        body = Line(Point(0, 50), Point(0, -100))
        body.setFill("black")
        body.setWidth(20)
        body.draw(puzzleWin)

        # Draw arms
        arms = [Line(Point(-100, 0), Point(100, 0))]

        # Draw legs
        legs = [Line(Point(0, -100), Point(-50, -200)), Line(Point(0, -100), Point(50, -200))]

        # Combine all body parts into a list
        body_parts = arms + legs

        # Draw all body parts in black
        for part in body_parts:
            part.setFill("black")
            part.setWidth(20)
            part.draw(puzzleWin)

        # Draw one square per body part
        for x, y in itemBoxCoords:
            itemBox = Rectangle(Point(x - 20, y - 20), Point(x + 20, y + 20)) 
            itemBox.setFill('grey')
            itemBox.draw(puzzleWin)

        # Draw 5 squares at the top of the window 
        # (here there will be the 5 inventory icons)
        for x, y in puzzleBoxCoords:
            puzzleBox = Rectangle(Point(x - 20, y - 20), Point(x + 20, y + 20))
            puzzleBox.setFill('grey')
            puzzleBox.draw(puzzleWin)

        # Initialize the buttons list
        buttons = []

        # Create button for each item in buttonParams
        for buttonName, params in buttonParams.items():
            if buttonName != "enterButton":
                # Create a Button instance with 'black' color if the buttonName is not "enterButton"
                button = Button(puzzleWin, Point(params[0], params[1]), 40, 40, params[2], 'black')
            # For "enterButton", create Button instance without specifying color
            button = Button(puzzleWin, Point(params[0], params[1]), 40, 40, params[2])
            # Add button to buttons list
            buttons.append(button)

        # Parameters for icons
        iconParams = [
            ("curiosity",        (-100, 200, "take")),
            ("acceptance",       (-50, 200, "take")),
            ("knowledge",        (0, 200, "take")),
            ("communication",    (50, 200, "take")),
            ("love",             (100, 200, "take")),

            ("curiosityBox",     (0, 150, "place")),       
            ("acceptanceBox",    (0, 0, "place")),         
            ("knowledgeBox",     (150, 0, "place")),        
            ("communicationBox", (-150, 0, "place")),       
            ("loveBox",          (0, -150, "place"))
            ]
        
        # Initialize the icons list
        icons = []

        # Create icons for each item in the first 5 elements of iconParams
        for name, params in iconParams[:5]:
            name = Image(Point(params[0], params[1]), f"gameFinalProject\images\item-{name}.png")
            # Add icon to icons list
            icons.append(name)

        # Initialize puzzleOver flag
        puzzleOver = False

        # Keep running the puzzle until puzzleOver is set to True
        while not puzzleOver:
            # Wait for a mouse click
            puzzleWin.getMouse()

            # Check if any of the first 5 buttons are clicked
            for button in buttons[:5]:
                if button.clicked(puzzleWin.getMouse()):
                    # If a button is clicked, create a red rectangle around the button
                    selectRect = Rectangle(
                        Point(buttonParams[button.getLabel()][0] - 20, 
                              buttonParams[button.getLabel()][1] - 20),
                        Point(buttonParams[button.getLabel()][0] + 20,
                              buttonParams[button.getLabel()][1] + 20))
                    selectRect.setOutline('red')
                    selectRect.draw(puzzleWin)
                    # Wait for another mouse click
                    puzzleWin.getMouse()

            # Wait for a mouse click
            puzzleWin.getMouse()

        print("Now print results")
        # When the Enter button is pressed... see the results of the puzzle
        # see_puzzle_results()

    # Say that you need 5 items in the inventory
    else:
        puzzleWin = GraphWin("Puzzle", 200, 200)
        notYetMessage = Text(Point(100, 100), f"You must have 5 items \nin you inventory")
        notYetMessage.draw(puzzleWin)
        puzzleWin.getMouse()
# puzzle_with_graphs(["curiosity", "acceptance", "knowledge", 'communication', 'love'], score = 0)

# Second prototype, simpler puzzle with only 5 buttons
score = 0
def puzzle_with_graphs(inventory, score):
    # return the score
    score = score + 1
    
    # Initiate puzzle
    puzzleWin = GraphWin("Puzzle", 400, 400)
    puzzleWin.setBackground("black")
    puzzleWin.setCoords(-200, -200, 200, 200)
    buttonParams = {
        "curiosity":  (-100, 100),
        "knowledge":  (-100, -100),
        "communication": (100, -100),
        "acceptance": (100, 100),
        "love":       (0, 0),
    }
    
    
    # Draw head
    head = Circle(Point(0, 100), 50)
    head.setFill("grey")
    head.draw(puzzleWin)

    # Draw body
    body = Line(Point(0, 50), Point(0, -100))
    body.setFill("grey")
    body.setWidth(20)
    body.draw(puzzleWin)

    # Draw arms
    arms = [Line(Point(-100, 0), Point(100, 0))]

    # Draw legs
    legs = [Line(Point(0, -100), Point(-50, -200)), Line(Point(0, -100), Point(50, -200))]

    # Combine all body parts into a list
    body_parts = arms + legs

    # Draw all body parts in black
    for part in body_parts:
        part.setFill("grey")
        part.setWidth(20)
        part.draw(puzzleWin)


    buttons = {item: Button(puzzleWin, Point(*buttonParams[item]), 60, 60, item) for item in inventory}
    for button in buttons.values():
        button.activate()

    correct_sequence = ['curiosity', 'knowledge', 'communication', 'acceptance', 'love']
    player_sequence = []

    while len(player_sequence) < 5:
        clickPoint = puzzleWin.getMouse()  # Store the click point
        for item, button in buttons.items():
            if button.clicked(clickPoint):  # Check the click point with each button
                player_sequence.append(item)
                button.deactivate()
                break


    if player_sequence == correct_sequence:
        result = Text(Point(0, 170), "You have solved the puzzle!")
        result.setStyle("bold")
        result.setTextColor("light green")

        # terminate the game (Finally!!)
        gameOver = True

        # Display the message with
        # intermitence with delay to
        # EVOKE ENTHUSIASM!!!!!
        for i in range(2):
            result.draw(puzzleWin)
            time.sleep(0.1)
            result.undraw()
            time.sleep(0.1)
        
        # draw again the result
        result.draw(puzzleWin)

    else:
        result = Text(Point(0, 170), "That's not correct. Try again!")
        result.setStyle("bold")
        result.setTextColor("red")
        
        # not terminate the game yet (Awwww!!)
        gameOver = False
        result.draw(puzzleWin)

    time.sleep(0.9)  # keep the window open for a bit
    puzzleWin.close()
    return score, gameOver

# score = puzzle_with_graphs(["curiosity", "acceptance", "knowledge", 'communication', 'love'], score = 0)
# print(score)
# Solve the puzzle
def puzzle(player, inventory, score):
    mistakes = 0
    
    # v Uncomment only for testing v
    # inventory = [
    #     "curiosity",
    #     "acceptance",
    #     "knowledge",
    #     "communication",
    #     "love"
    #     ]
    
    print(f"Oh! So you want to solve this puzzle? Well..")
    if len(inventory) == 5:
        # Add a puzzle attempt to the score marker
        score += 1
        # Display the explanation of the puzzle
        print(f"It seems that you have all the items of this world")
        print(f"You see a human-shaped figure in front of you...")
        print(f"You have 5 spaces on where to put the items you collected, you just have to type")
        print(f"the name of the item in the space you think it's correct")
        head        = input("Head? >> ")
        chest       = input("Chest? >> ")
        leftArm     = input("Left Arm? >> ")
        rightArm    = input("Right Arm? >> ")
        legs        = input("Legs? >> ")

        # Set the puzzle key
        puzzleKey = [
            (head, "knowledge"), 
            (chest, "love"), 
            (leftArm, "communication"), 
            (rightArm, "acceptance"), 
            (legs, "curiosity")]

        # verify the answers
        for (part, item) in puzzleKey:
            if str(part) != str(item):
                mistakes += 1
        # if after going through every answer there are no mistakes...
        if mistakes == 0:
            print(f"\n\n====== You completed the game! =======")
            print(f"Congratulations! You have solved the puzzle!")
            print(f"Thanks for your increadible journey through this")
            print(f"amazing adventure! I hope to see you again soon!")
            print(f"\nYour score was.... {score}\nRemember: The lower the score, the better!!")
            print(f"Although it can't be 0.. right? anyway good work!!!")

            # Finish the game!
            gameOver = True
            return gameOver
        
        else:
            # Ask to solve the puzzle again or not
            print(f"seems you have {mistakes} mistakes... come on, try again!")
            ans = input(f"you want to try again? (y/n) >> ")
            if ans == "y":
                puzzle(player, inventory, score)
            else:
                pass
        
        # else, if the len(inventory) is not 5
    else:
        print("You seem to not have all the items\nin your inventory\nRemember, there are 5 items")


def show_puzzle_intro():
    # Create the window
    window = GraphWin("Puzzle Instructions", 400, 400)
    window.setBackground("black")
    # Create the text message
    message = Text(Point(200, 150), 
                   "Reflect on human growth: we begin with \na burning curiosity that sparks our\n"
                   "desire for knowledge. With knowledge, \nwe develop the skills to communicate,\n"
                   "which opens the path to acceptance. \nIn the end, we discover that all paths\n"
                   "lead towards the ultimate goal: love.")
    message.setTextColor("white")
    message.setStyle('bold')
    message.draw(window)

    # Create the "Start Puzzle" button
    start_puzzle_button = Button(window, Point(140, 300), 100, 50, "Start\nPuzzle")
    start_puzzle_button.activate()

    # Create the "Go Back" button
    go_back_button = Button(window, Point(260, 300), 70, 50, "Go\nBack")
    go_back_button.activate()

    openPuzzle = None

    # Wait for a button click
    while openPuzzle is None:
        clickPoint = window.getMouse()

        if start_puzzle_button.clicked(clickPoint):
            openPuzzle = True
        elif go_back_button.clicked(clickPoint):
            openPuzzle = False

    window.close()
    
    return openPuzzle
# You can call the function like this 
# !!! this is only for testing:
# openPuzzle = create_window_with_message()

def final_window(score):
    # Create a new Graphics Window titled "Congratulations!" with size 400x400 pixels
    finalWin = GraphWin("Congratulations!", 400, 400)

    # Set the coordinate system in the Graphics Window to span from -250 to 250 on both axes
    finalWin.setCoords(-250, -250, 250, 250)

    # Set the background color of the Graphics Window to dark blue
    finalWin.setBackground("dark blue")

    # Formulate the final message including the player's score
    message = f"Congratulations!!!\nYou completed A mind's Journey!\nI hope you had a pleasant gaming experience\n\nThis game was made entirely by \nRonald Beltran.\nIEU BCSAI Freshman\n\nThanks for playing!\nBy the way your score was {score}\nthe lower, the better"

    # Create a Text object at the center of the Graphics Window with the final message
    finalText = Text(Point(0, 0), message)

    # Set the properties (size, style, face, and color) of the Text object
    finalText.setSize(10)
    finalText.setStyle('bold')
    finalText.setFace('helvetica')
    finalText.setTextColor('white')

    # Draw the Text object in the Graphics Window
    finalText.draw(finalWin)

    # Wait for a mouse click inside the Graphics Window before closing
    finalWin.getMouse()
# final_window()
