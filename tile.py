from graphics import *
import math


class Tile(Rectangle):

    """Inherits from Rectangle but adds among others a type-attribute to distinguish between walls, floors and goal"""

    def __init__(self, p1, p2, type, x, y):

        Rectangle.__init__(self, p1, p2)
        self.type = type        # Wall, floor, exit or player
        self.x = x              # X-coordinate in the two dimensional list
        self.y = y              # Y-coordinate in the two dimensional list
        self.distance = 0       # Distance to the goal, calculated after initialization
        self.parent = None
        self.travel_cost = 0    # Number of moves needed to reach the tile from the start
        self.total_cost = 0     # Equal to travel_cost*distance
        self.visited = False    # Boolean representing whether or not the tile has already been visited by the bot

    def set_distance(self, goal):

        """Sets the distance between a Tile-object and the goal tile"""

        self.distance = math.sqrt((self.x - goal.x) ** 2 + (self.y - goal.y) ** 2)


