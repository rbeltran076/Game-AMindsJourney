# The windows of the game
# Include the main interface, the menu, and the different rooms

import time
from Button import Button
from graphics import *
from objects import * 
from functions import *

class Menu:
    def __init__(self):            
        # Initializing a window object with a black background of size 600 x 600
        interfaceWin = GraphWin("Ronald Beltran's A Mind's Journey", 500, 500)
        interfaceWin.setCoords(-250, -250, 250, 250)
        interfaceWin.setBackground('dark blue')

        # Set the texts for the menu window
        texts = [
            ("A mind's Journey", 1, 150),
            ("A game by Ronald Beltrán", 1, 120)
            ]

        for text, x, y in texts:
            # Adding a white text display at the upper center
            text = Text(Point(x, y), text)
            text.setSize(15)
            text.setFace('helvetica')
            text.setTextColor('white')
            text.draw(interfaceWin)

        # Add the "Start" button, if pressed, then the window changes to 
        # another black window
        startButton = Button(interfaceWin, Point(1, 1), 100, 40, "Start")
        introButton = Button(interfaceWin, Point(1, -50), 100, 40, "Introduction")

        # Defining a list of the buttons to automate the customization
        buttons = [startButton, introButton]

        for button in buttons:
            button.activate()
        
        # TODO: Temporary code to solve after I finish the game itself
        # Wait for the user to press 'q' to quit
        while not startButton.clicked(interfaceWin.getMouse()):
            if introButton.clicked(interfaceWin.getMouse()):
                introWin = GraphWin("Introduction", 500, 500)
                introWin.setCoords(-250, -250, 250, 250)
                introWin.setBackground('black')

                # Create a "next" button that passes to the next part
                nextButton = Button(introWin, Point(200, -200), 60, 40, "--->")
                nextButton.activate()


                introParts = [
                    "Greetings, dear traveler, \nand welcome to an extraordinary \nquest you've stumbled upon!",
                    "\"A Mind's Journey\"\n - a world unique in its essence awaits you. \nThis isn't just a mere realm you're about to explore, \nbut a landscape of human values, \nmanifesting themselves through the enigma of \nsix meticulously crafted rooms.",
                    "Brace yourself, for in each room, \nyou'll encounter an item, a symbolic representation of \nsomething deeply entrenched in the human experience. \nYour mission, should you choose to accept it, \nis to gather all five inventory.",
                    "But that's not all! \nThe final room will challenge you with a puzzle,\n a test of wisdom and bravery, and \nsuccess will bring you nothing less than triumph. \nSo, get ready! On this journey, \nevery decision matters, \nevery step resonates. \nEmbrace the challenge, \nand may the journey forge you into a hero!"
                    ]

                for part in introParts:
                    introText = Text(Point(1, 1), part)
                    introText.setSize(15)
                    introText.setFace('helvetica')
                    introText.setTextColor('white')
                    introText.draw(introWin)
                    if nextButton.clicked(introWin.getMouse()):
                        pass
                    introText.undraw()
                introWin.close()           
        interfaceWin.close()

# Creating the class "Interface" which will be the main window where the things happen
class Interface:
    # Initiate the main interface window knowing which room the player is in 
    # and the state of the player
    def __init__(self, room, inventory, isPuzzle, score):
        # define each attribute
        # self.rooms = rooms
        self.room = str(room)
        self.inventory = inventory
        self.isPuzzle = bool(isPuzzle)

        # set the structure of the interface 
        # with a text display on the bottom
        # and an image space at the top
        interfaceWin = GraphWin("Ronald Beltran's A Mind's Journey", 800, 500)
        interfaceWin.setCoords(-300, -300, 300, 300)
        interfaceWin.setBackground('black')
        
        # setting the image filepath according to the name of the room
        imageFilepath = str(f"gameFinalProject/images/room-{self.room}.png")

        # Adding an image to the top half of the window.
        # The image will be centered in the upper half of the window
        # and will be scaled to fit the size of the window
        image = Image(Point(130, 0), imageFilepath)
        image.draw(interfaceWin)

        # Make a line separator below the margin, right at the middle
        lineSeparator = Line(Point(-270, -60), Point(-30, -60))
        lineSeparator.setFill("dark red")
        lineSeparator.draw(interfaceWin) 

        # Adding a white text display at the center
        # The text2 that will be displayed
        message = f"""This is the {get_data('room', self.room, 'name')}.
{get_data('room', self.room, 'description')}

Items that can be collected here:
{get_data('room', self.room, 'item') if room != 'start' else 'Here you cannot find any items'}.
{get_data('item', self.room, 'description') if room != 'start' else ''}
"""
        # Create Text object with message content
        bigText = Text(Point(-150, 80), message)
        bigText.setSize(10)
        bigText.setStyle('bold')
        bigText.setFace('helvetica')
        bigText.setTextColor('white')
        bigText.draw(interfaceWin)

        # Display an initial action message2
        message2 = f"""Commands available:
look [north, south, ease, west, up, down]
move [north, south, east, west]
get <item>
inventory
map"""

        text2 = Text(Point(-150, -200), message2)
        text2.setSize(10)
        text2.setStyle('bold')
        text2.setFace('helvetica')
        text2.setTextColor('white')
        text2.draw(interfaceWin)

        # An entry type object to input the player movements
        # with black background and white letters
        entry = Entry(Point(-180, -100), 20)
        entry.setTextColor("white")
        entry.setFill("black")
        entry.setFace('helvetica')
        entry.draw(interfaceWin)

        # A button to read the Entry object's text
        entryButton = Button(interfaceWin, Point(-80, -100), 40, 30, "Enter")
        entryButton.activate()

        # Run as long as the room does not change
        while self.room == room:
            # If the window is associated with the puzzle room and all items are collected
            if self.isPuzzle == True and len(inventory) == 5:
                # Draw a "Solve Puzzle" button in the interface window
                puzzleButton = Button(interfaceWin, Point(-150, -40), 50, 40, "Solve\nPuzzle")
                # Activate the button
                puzzleButton.activate()
                # If the button is clicked
                if puzzleButton.clicked(interfaceWin.getMouse()):
                    # Show the puzzle introduction
                    startPuzzle = show_puzzle_intro()
                    if startPuzzle == True:
                        # Execute the puzzle and update the score
                        score, gameOver = puzzle_with_graphs(inventory, score)
                        # If the game is over
                        if gameOver == True:
                            # Close the interface window and show the final window
                            interfaceWin.close()
                            final_window(score)
                    else:
                        pass
            # If the window is associated with the puzzle room but not all items are collected
            elif self.isPuzzle and len(inventory) != 5:
                # Display a message prompting the player to collect all items
                text = Text(Point(-150, -40), "Collect all items\nto solve the puzzle!")
                text.setTextColor('cyan')
                text.setSize(10)
                text.setStyle('bold')
                text.draw(interfaceWin)

            # If th entry button is clicked...
            if entryButton.clicked(interfaceWin.getMouse()):
                # Get the text from the Entry and store it as "input"
                input = entry.getText().lower().split(" ")

                # if the input starts with "l", command look sequence
                if input == None:
                    message = f"Em.. yeah, enter a command!!"
                    text = Text(Point(-150, -45), message)
                    text.setSize(10)
                    text.setStyle('bold')
                    text.setTextColor('red')
                    text.draw(interfaceWin)
                    time.sleep(0.7)
                    text.undraw()   
                
                elif input[0] == "look":
                    # Define a list with the only valid directions of the game
                    validDirections = ["north", "south", "east", "west", "up", "down"]

                    # take the second word from the input
                    direction = input[1]

                    # undraw the initial message
                    # update the message that will be displayed below the Entry
                    bigText.undraw()

                    # if the direction entered is not valid...
                    if direction not in validDirections:
                        # set the message to determine so
                        message = f"Um hahah.. look where?"
                    else:
                        # Else, describe what is in that direction
                        message = f"{get_data('room', f'{self.room}', direction)}"            

                    # display the text that was set in the if statement. 
                    bigText = Text(Point(-150, 100), message)
                    bigText.setSize(10)
                    bigText.setStyle('bold')
                    bigText.setTextColor('white')
                    bigText.draw(interfaceWin)

                    
                # if the input starts with "g", command look sequence
                elif input[0] == "get":
                    # Define the list of possible items to get
                    itemsToGet = [
                        "curiosity", 
                        "acceptance", 
                        "knowledge", 
                        "communication", 
                        "love"
                        ]

                    # take the second word from the input
                    item = input[1]

                    if (item in itemsToGet) and (item == room) and (item not in inventory):
                        self.inventory = get_with_graphs(self.inventory, item)

                        # update the message that will be displayed below the Entry
                        message = f"You now have {item}!\n{get_data('item', f'{self.room}', 'description')}"             
                        getText = Text(Point(-150, 100), message)
                        getText.setSize(10)
                        getText.setStyle('bold')
                        getText.setTextColor('light green')

                        # Delete the bigText to replace it with the getText
                        bigText.undraw()
                        getText.draw(interfaceWin)

                        # return to bigText after 5 seconds
                        time.sleep(1.5)
                        getText.undraw()
                        bigText.draw(interfaceWin)

                    elif item in inventory:
                        message = f"You already have {item}"             
                        getText = Text(Point(-150, -45), message)
                        getText.setSize(10)
                        getText.setStyle('bold')
                        getText.setTextColor('orange')
                        getText.draw(interfaceWin)

                        time.sleep(1.5)
                        getText.undraw()

                    elif item in itemsToGet and item != room:
                        message = f"Maybe {item} is in another room.."             
                        getText = Text(Point(-150, -45), message)
                        getText.setSize(10)
                        getText.setStyle('bold')
                        getText.setTextColor('orange')
                        getText.draw(interfaceWin)

                        time.sleep(1.5)
                        getText.undraw()

                    else:
                        message = f"Haha, yeah umm.. there is no item named like that."             
                        getText = Text(Point(-150, -45), message)
                        getText.setSize(10)
                        getText.setStyle('bold')
                        getText.setTextColor('red')
                        getText.draw(interfaceWin)
                        
                        time.sleep(1.5)
                        getText.undraw()
                
                    
                # if the input starts with "m", command move sequence
                # when we want to move and are in the graphics version.
                # i think its better to initiate another interface.
                elif input[0] == "move":
                    
                    # define the 4 valid directions to move
                    validDirections = ["north", "south", "east", "west"]

                    # get the second word as direction
                    reposition = input[1]

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
                    if reposition in rooms[self.room]:
                        self.room = rooms[self.room][reposition]
                        interfaceWin.close()
                        break

                    else:
                        # if the command's direction is not a direction of an exit..
                        bigText.undraw()

                        # tell the player that there is not a direction to go
                        message = f"There is no space to go in that direction."
                        text = Text(Point(-150, 100), message)
                        text.undraw()
                        text.setSize(10)
                        text.setStyle('bold')
                        text.setTextColor('red')
                        text.draw(interfaceWin)

                        # Leave the text in screen for 1 second and return
                        # to the original message.
                        time.sleep(1)
                        text.undraw()
                        bigText.draw(interfaceWin)

                # Elif the command is for the seeing inventory...
                elif input[0] == "inventory":
                    # Define the inventory
                    items = [
                        "curiosity",
                        "acceptance",
                        "knowledge",
                        "communication",
                        "love",
                        ]

                    # Create the inventory window
                    inventoryWin = GraphWin("Inventory", 250, 350)
                    inventoryWin.setBackground("dark red")

                    message = "Click anywhere to exit"
                    text = Text(Point(125, 330), message)
                    text.setTextColor('light grey')
                    text.draw(inventoryWin)
                    
                    # Define the initial position for the first square
                    x_pos = 50
                    y_pos = 50

                    # Draw the squares and the corresponding texts
                    for i in range(len(items)):
                        # Draw square
                        square = Rectangle(Point(x_pos, y_pos), Point(x_pos + 50, y_pos + 50))
                        square.setFill("black")
                        square.setOutline("white")
                        square.draw(inventoryWin)

                        # Draw text
                        item_text = Text(Point(x_pos + 25, y_pos - 10), items[i])
                        item_text.setTextColor('light grey')
                        item_text.draw(inventoryWin)

                        # Update the x position for the next square. You can change the value to adjust the spacing between squares.
                        x_pos += 100

                        # After drawing 2 squares in a row, move to the next row
                        if (i+1) % 2 == 0:
                            y_pos += 100
                            x_pos = 50

                    # Draw images on the squares corresponding to the acquired inventory
                    for item in inventory:
                        item_index = items.index(item)
                        # Calculate the square's x and y positions
                        x_pos = 50 + 100 * (item_index % 2)
                        y_pos = 50 + 100 * (item_index // 2)
                        # Create the filepath
                        filepath = f"gameFinalProject\images\item-{item}.png"
                        # Create and draw the image
                        img = Image(Point(x_pos + 25, y_pos + 25), filepath)
                        img.draw(inventoryWin)

                    # close after a click in the window
                    inventoryWin.getMouse()
                    inventoryWin.close()
                elif input[0] == 'map':
                    mapWin = GraphWin("Map", 400, 400)
                    mapWin.setBackground("black")
                    mapWin.setCoords(-200, -200, 200, 200)
                    
                    # show the image from the images folder
                    map = Image(Point(0, 0), "gameFinalProject\images\map.png")
                    map.draw(mapWin)

                    # wait for the window to be clicked 
                    mapWin.getMouse()
    
    # get the current room
    def getRoom(self):
        return self.room

# testing area ==================================
# menu = Menu()
# interface = Interface("puzzle", ["curiosity", ])
# compass = Compass()