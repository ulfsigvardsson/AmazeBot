from graphics import *
import math
from tile import *


def has_neigbour_floor(list, x, y):
    """Determines if a tile has neighbouring floors, to be used for maze generation"""

    neighbourlist = neighbour_list(list, x, y)
    for neighbour in neighbourlist:
        if neighbour.type == "Floor":
            return True
        #TODO: connect to a maze generating function


def neighbour_list(list, x, y):
    """Returns a list of all neighbouring tiles in four directions"""

    neighbours = [list[x][y + 1], list[x][y - 1], list[x + 1][y], list[x - 1][y]]

    return neighbours

def paint_path(tile):
    """Prints the optimal path towards the goal by back-tracking from the goal tile"""

    if tile.type=="Start":      # If it is the start tile, reverse the list
        path.reverse()

        for tile in path:       # Then follow the path to the goal
            time.sleep(0.05)
            if tile.type == "Exit":
                tile.setFill("green")
            else:
                tile.setFill("yellow")
    else:
        path.append(tile.parent)
        paint_path(tile.parent)


def findpath(tile, x, y):
    """Moves the 'player' through the maze

       tile:: Tile-object representing the current position
       x:: integer, x-coordinates of 'tile'
       y:: integer, y-coordinates of 'tile'    """

    closed_list.append(tile)

    if tile in open_list:
        open_list.remove(tile)      # Make tile uneligible for future consideration
    if tile.type == "Exit":
        path.append(tile)
        paint_path(tile)
        w1.getMouse()   # Keeps the window from closing
        quit()

    else:
        tile.set_status("Visited")
        neighbours = neighbour_list(row_list, x, y)     # Finds all neighbouring tiles
                                                        # and returns them in a list


        for neighbour in neighbours:
            if neighbour.type != "Wall" and neighbour.status != "Visited":
                open_list.append(neighbour)             # Adds all valid neighbours to open_list
                neighbour.set_parent(tile)

        open_list.sort(key=lambda x: x.distance)    # Sorts the list of open tiles by distance to goal

        new_tile = open_list[0]
        findpath(new_tile, new_tile.get_x(), new_tile.get_y())  # Runs the findpath() function on the open tile
                                                                # closest to the goal

        # TODO: remove yellow color for every 'wrong' branch
def make_goal(tile):
    """Establishes a goal tile and returns its coordinates

       tile:: a Tile-object"""

    x = tile.get_x()
    y = tile.get_y()
    coordinates=Point(x, y)
    tile.setFill("red")
    tile.type="Exit"
    return coordinates

#  ==============================================================================================
#                                       MAIN METHOD
#  ==============================================================================================

map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
] # A hard-coded map

# CONSTANTS, DO NOT CHANGE THESE!!!
ROWS = 20
COLUMNS = 20
WINDOWHEIGHT = 500
WINDOWBREADTH = 500
TILESIZE = WINDOWBREADTH/COLUMNS

w1 = GraphWin("Maze", WINDOWHEIGHT, WINDOWBREADTH)
row_list = []       # List to contain every list of columns
goal = None         # Declared in main scope for availability
start = None        # Declared in main scope for availability
open_list=[]        # Tracks all current path options
closed_list=[]      # Tracks all exhausted paths
path=[]

for i in range(len(map)):   # Outer loop for generating every row
    column_list = []        # List set to empty for a iteration of a new row

    for j in range(len(map[i])):   # Inner loop to iterate every column on each row

        # Tile object are created as floors by default
        r = Tile(Point(i*TILESIZE, j*TILESIZE), Point((i+1)*TILESIZE, (j+1)*TILESIZE), "Floor", i, j)

        if map[j][i] == 1:  # Paints the tiles according to the map
            r.setFill("black")
            r.set_type("Wall")

        elif map[j][i] == 3:
            r.setFill("blue")
            r.set_type("Start")
            start = r

        elif map[j][i] == 2:
            r.setFill("red")
            r.set_type("Exit")
            goal = r
            goal_coords = make_goal(goal)   # Sets coordinates for the goal tile

        column_list.append(r)   # Append each rectangle to its list of columns
        r.draw(w1)

    row_list.append(column_list)    # Append each list to the list of rows

# Sets the distance-to-goal-attribute for each tile on the map
for i in range(len(row_list)):
    for j in range(len(column_list)):
        row_list[i][j].set_distance(goal)

#TODO: write a maze generating function ta determine the exit tile before storing them in an array.

findpath(start, start.get_x(), start.get_y())   # Starts the maze bot
w1.getMouse()