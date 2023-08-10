# the classes and objects intitializations for main.py

# The player has the attributes of inventory
class Player:
    def __init__(self, inventory, orientation, position):
        self.inventory = list(inventory)

        # Rules for naming things:
        # self.position should only say the room's theme (start)
        # self.orientation and position should always be lowercase.
        self.orientation = orientation
        self.position = position
    
    def getOrientation(self):
        return self.orientation

    def getPosition(self):
        return str(self.position)

    # Change the orientation with commands
    def reorient(self, direction):
        self.orientation = direction

    # Change the position of the player with commands
    def reposition(self, newPosition):
        self.position = newPosition