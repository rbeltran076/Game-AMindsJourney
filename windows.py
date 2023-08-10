# The windows of the game
# Include the main interface, the menu, and the different rooms

from graphics import *
from Button import Button

class Menu:

    def __init__(self):

        # Initializing a window object with a black background of size 600 x 600
        win = GraphWin("Ronald Beltran's A Mind's Journey", 600, 600)
        win.setCoords(-300, -300, 300, 300)
        win.setBackground('black')

        # Adding a white text display at the upper center
        text = Text(Point(1, 150), "A mind's Journey")
        text.setSize(20)
        text.setStyle('bold')
        text.setFace('helvetica')
        text.setTextColor('white')
        text.draw(win)

        # Add the "Start" button, if pressed, then the window changes to 
        # another black window
        startButton = Button(win, Point(1, 1), 200, 200, "Start")
        startButton.labelColor = 'white'
        startButton.labelFont = 'helvetica'
            
        # TODO: Temporary code to solve after I finish the game itself
        # Wait for the user to press 'q' to quit
        while win.getKey() != "q" or not startButton.active:
            key = win.getKey()



# Creating the class "Interface" which will be the main window where the things happen
class Interface:
    def __init__(self):
        # set the structure of the interface 
        # with a text display on the bottom
        # and an image space at the top
        win = GraphWin("Ronald Beltran's A Mind's Journey", 600, 600)
        win.setCoords(-300, -300, 300, 300)
        win.setBackground('black')
        
        # Adding a white text display at the center
        # The message that will be displayed
        message = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua"""
        # The characteristics of the text object.
        text = Text(Point(1, -130), message)
        text.setSize(15)
        text.setStyle('bold')
        text.setFace('helvetica')
        text.setTextColor('white')
        text.draw(win)

        # Adding the image display at the upper half
        # of the screen
        image = Image(Point(-150, -150), "programming/gameFinalProject/images/readme-main-map.jpg")
        image.draw(win)
        # TODO: Temporary code to solve after I finish the game itself
        # Wait for the user to press 'q' to quit
        while win.getKey() != "q":
            key = win.getKey()


# TODO. creating the class compass (still unsure) to make the 
class Compass:
    def __init__(self):
        # Initialize a small window object of 75 x 75 with only an image
        # display
        win = GraphWin("Ronald Beltran's A Mind's Journey", 75, 75)
        win.setCoords(-75, -75, 75, 75)
        win.setBackground('black')
