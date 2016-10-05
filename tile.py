from graphics import *
import math

class Tile(Rectangle):
    """Derives from Rectangle but adds among others a type-attribute to distinguish between walls, floors and goal"""
    status = "undiscovered" # Initial status for all tiles
    distance = 0    # Initial distance for all tiles

    def __init__(self, p1, p2, type, x, y):     # Constructor
        Rectangle.__init__(self, p1, p2)
        self.type = type
        self.x = x
        self.y = y

    def get_type(self):
        """Returns the type-attribute of a Tile-object"""
        return self.type

    def get_status(self):
        """Returns the status-attribute of a Tile-object"""
        return self.status

    def set_type(self, type):
        """Sets the type-attribute of a Tile-object"""
        self.type=type

    def set_status(self, status):
        """Sets the status-attribute of a Tile-object"""
        self.status=status

    def get_x(self):
        """Returns the x-coordinate of a Tile-object"""
        return  self.x

    def get_y(self):
        """Returns the y-coordinate of a Tile-object"""
        return self.y

    def get_distance(self):
        """Returns the distance between a Tile-object and the goal tile"""
        return self.distance

    def set_distance(self, goal):
        """Sets the distance between a Tile-object and the goal tile"""
        self.distance = math.sqrt((self.get_x() - goal.get_x()) ** 2 + (self.get_y() - goal.get_y()) ** 2)


