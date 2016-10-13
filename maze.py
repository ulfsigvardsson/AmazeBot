from tile import *
import pygame
pygame.init()



# =============================================
#                   FUNCTIONS
# =============================================

def neighbour_list(x, y):

    """Returns a list of all neighbouring tiles in four directions

        x:: integer, x-coordinate of a Tile-object
        y:: integer, y-coorfinate of a Tile-object"""

    neighbours = [
                    row_list[x][y + 1],
                    row_list[x][y - 1],
                    row_list[x + 1][y],
                    row_list[x - 1][y]
    ]

    return neighbours


def paint_path(tile):

    """Prints the optimal path towards the goal by back-tracking from the goal tile

    tile:: instance of Tile"""

    if tile.type == "Player":      # If it is the player tile, reverse the list

        path.reverse()


        for tile in path:          # Then follow the path to the goal

            time.sleep(0.01)

            if tile.type == "Exit":
                tile.setFill("green")

            else:
                tile.setFill("yellow")

    else:
        path.append(tile.parent)
        paint_path(tile.parent)


def solve(tile, x, y):

    """Moves the 'player' through the maze

       tile:: Tile-object representing the current position
       x:: integer, x-coordinates of 'tile'
       y:: integer, y-coordinates of 'tile'    """

    closed_list.append(tile)

    if tile in open_list:
        open_list.remove(tile)                  # Make tile uneligible for future consideration


    if tile.type == "Exit":
        path.append(tile)
        paint_path(tile)
        w1.getMouse()                           # Keeps the window from closing
        quit()

    else:
        tile.set_status("Visited")
        neighbours = neighbour_list(x, y)       # Finds all neighbouring tiles
                                                # and returns them in a list


        for neighbour in neighbours:

            if neighbour.type != "Wall" and neighbour.status != "Visited":
                open_list.append(neighbour)     # Adds all valid neighbours to open_list
                neighbour.set_parent(tile)
                neighbour.cost = tile.cost+1      # Increment the travel cost of the neighbours by one

                neighbour.total_cost = neighbour.cost*neighbour.distance    # Set total cost to travel cost
                                                                            # times distance to goal

        open_list.sort(key=lambda x: x.total_cost)    # Sorts the list of open tiles by distance to goal

        new_tile = open_list[0]
        solve(new_tile, new_tile.get_x(), new_tile.get_y())  # Runs the solve() function on the open tile
                                                                # closest to the goal


def make_goal(tile):

    """Establishes a goal tile and returns its coordinates

       tile:: a Tile-object"""

    x = tile.get_x()            # x-coordinates for the tile
    y = tile.get_y()            # y-coordinates for the tile
    coordinates = Point(x, y)   # Coordinates for the goal tile as a Point()
    tile.setFill("red")
    tile.type = "Exit"
    return coordinates


def make_maze():

    """Generates a list of tile-objects with attributes according to the hard coded map"""

    for i in range(len(map)):  # Outer loop for generating every row
        column_list = []  # List set to empty for a iteration of a new row

        for j in range(len(map[i])):  # Inner loop to iterate every column on each row

            # Tile object are created as floors by default
            r = Tile(
                Point(i * TILESIZE, j * TILESIZE),  # Upper corner of Tile
                Point((i + 1) * TILESIZE, (j + 1) * TILESIZE),  # Lower corner of Tile
                "Floor",  # Tile type
                i,  # x-coordinate in the grid
                j  # y-coordinate in the grid
            )

            # Paints the tiles according to the map

            if map[j][i] == 1:

                r.setFill("black")
                r.set_type("Wall")


            elif map[j][i] == 3:


                r.setFill("blue")
                r.set_type("Player")
                # Player tile, not yet implemented




            elif map[j][i] == 2:

                r.setFill("red")
                r.set_type("Exit")
                goal = r
                goal_coords = make_goal(goal)  # Sets coordinates for the goal tile

            column_list.append(r)  # Append each rectangle to its list of columns
            r.draw(w1)

        row_list.append(column_list)  # Append each list to the list of rows

        # Sets the distance-to-goal-attribute for each tile on the map
    for i in range(len(row_list)):

        for j in range(len(column_list)):
            row_list[i][j].set_distance(goal)


def callback(event):

    """Event handler for click events, sets focus to the display screen"""

    w1.focus_set()


def key(event):

    """Event handler for pressed keys"""

    current=get_current()                       # Get the current player tile
    x=current.get_x()                           # Get the x-coordinate
    y=current.get_y()                           # Get the y-coordinate

    if x>0 and x<COLUMNS and y>0 and y<ROWS:    # Check if it's possible to make a move within the boundaries of the map
        up = row_list[x][y-1]
        down = row_list[x][y+1]
        left = row_list[x-1][y]
        right = row_list[x+1][y]

        if event.keysym == "s":                   # If 's' is pressed, the bot solves the maze
            solve(current, x, y)

        if event.keysym == "Up":                  # If any of the arrow keys are pressed,
                                                  # move accordingly
            if up.type != "Wall":
                up.setFill("blue")
                up.type = "Player"
                current.setFill("white")
                current.type = "Floor"

        if event.keysym == "Down":

            if down.type != "Wall":
                down.setFill("blue")
                down.type = "Player"
                current.setFill("white")
                current.type = "Floor"

        if event.keysym == "Left":

            if left.type != "Wall":
                left.setFill("blue")
                left.type = "Player"
                current.setFill("white")
                current.type = "Floor"

        if event.keysym == "Right":

            if right.type != "Wall":
                right.setFill("blue")
                right.type = "Player"
                current.setFill("white")
                current.type = "Floor"


def get_current():

    """Returns the current player tile from row_list"""

    for row in row_list:
        for tile in row:
            if tile.type == "Player":
                return tile



# =============================================
#                 BACKING FIELD
# =============================================

map = [                             #
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 3, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]         # A hard-coded map

ROWS = 40
COLUMNS = 40
WINDOWHEIGHT = 1000
WINDOWBREADTH = 1000
TILESIZE = WINDOWBREADTH/COLUMNS

w1 = GraphWin(
                "Maze",
                WINDOWHEIGHT,   # Height of window
                WINDOWBREADTH   # Breadth of window
)

row_list = []       # List to contain every list of columns
goal = None         # Declared in main scope for availability
start = None        # Declared in main scope for availability
open_list = []      # Tracks all current path options
closed_list = []    # Tracks all exhausted paths
path = []           # Stores the optimal path



# =============================================
#                   MAIN
# =============================================

make_maze()         # Display the initial map

while True:

    w1.bind("<Key>", key)               # Sends all key events to the event handler
    w1.bind("<Button-1>", callback)     # Sends all mouse events to the event handler, sets focus to the window
    w1.getMouse()                       # Prevents the window from closing
