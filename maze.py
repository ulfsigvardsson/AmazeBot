from tile import *
import pygame
pygame.init()

# =============================================
#                   FUNCTIONS
# =============================================


def neighbour_list(x, y):

    """Returns a list of all neighbouring tiles in four directions

        x:: integer, x-coordinate of a Tile-object
        y:: integer, y-coordinate of a Tile-object"""

    neighbours = []

    if x > 0:
        neighbours.append(maze[x - 1][y])
    if x < COLUMNS-1:
        neighbours.append(maze[x + 1][y])
    if y > 0:
        neighbours.append(maze[x][y - 1])
    if y < ROWS-1:
        neighbours.append(maze[x][y + 1])

    return neighbours


def paint_path(tile):

    """Prints the optimal solution towards the goal by back-tracking from the goal tile when found

    tile:: instance of Tile"""

    if tile.type == "Player":      # If it is the player tile, reverse the list

        solution.reverse()


        for tile in solution:          # Then follow the solution to the goal

            time.sleep(0.03)

            if tile.type == "Goal":
                tile.setFill("green")

            else:
                tile.setFill("yellow")

    else:
        solution.append(tile.parent)    # Else continue traverse the solution
        paint_path(tile.parent)


def solve_maze(tile, x, y):

    """Solves the maze from the current tile

       tile:: Tile-object representing the current position
       x:: integer, x-coordinates of 'tile'
       y:: integer, y-coordinates of 'tile'    """


    if tile in open_list:
        open_list.remove(tile)                  # Make tile uneligible for future consideration


    if tile.type == "Goal":
        solution.append(tile)
        paint_path(tile)
        w1.getMouse()                           # Keeps the window from closing
        quit()

    else:
        tile.visited = True
        neighbours = neighbour_list(x, y)       # Finds all neighbouring tiles
                                                # and returns them in a list

        for neighbour in neighbours:

            if neighbour.type != "Wall" and not neighbour.visited:

                open_list.append(neighbour)     # Adds all valid neighbours to open_list

                if not neighbour.type == "Goal":
                    neighbour.setFill("orange")
                    time.sleep(0.001)

                neighbour.parent = tile
                neighbour.travel_cost = tile.travel_cost+1           # Increment the travel_cost of the neighbours by one
                neighbour.total_cost = neighbour.travel_cost*neighbour.distance    # Set total travel_cost to travel travel_cost
                                                                                   # times distance to goal

        open_list.sort(key=lambda x: x.total_cost)                   # Sorts the list of open tiles by distance to goal

        closest_tile = open_list[0]
        solve_maze(closest_tile, closest_tile.x, closest_tile.y)     # Runs the solve_maze() function on the open tile
                                                                     # closest to the goal


def display_maze():

    """Generates a list of tile-objects with attributes according to the hard coded map"""

    for i in range(len(map)):  # Outer loop for generating every row
        row = []  # List set to empty for a iteration of a new row

        for j in range(len(map[i])):  # Inner loop to iterate every column on each row

            # Tile object are created as floors by default
            r = Tile(
                Point(i * TILE_SIZE, j * TILE_SIZE),  # Upper corner of Tile
                Point((i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE),  # Lower corner of Tile
                "Floor",  # Tile type
                i,  # x-coordinate in the grid
                j  # y-coordinate in the grid
            )

            # Paints the tiles according to the map

            if map[j][i] == 1:

                r.setFill("black")
                r.type = "Wall"

            elif map[j][i] == 3:

                r.setFill("blue")
                r.type = "Player"
                # Player tile, not yet implemented

            elif map[j][i] == 2:

                r.setFill("red")
                r.type = "Goal"
                goal = r

            row.append(r)  # Append each tile to its row
            r.draw(w1)

        maze.append(row)  # Append each row to the list of rows

        # Sets the distance-to-goal-attribute for each tile on the map
    for i in range(len(maze)):

        for j in range(len(row)):
            maze[i][j].set_distance(goal)


def callback(event):

    """Event handler for click events, sets focus to the display screen

        event:: a mouse click event"""

    w1.focus_set()


def move_player(tile, current):

    """Switches attributes between the player tile and the floor tile beeing moved to

        tile:: Tile-object, the tile being moved to
        current:: Tile-object, the player tile"""

    if tile.type != "Wall":

        if tile.type == "Goal":
            tile.setFill("green")
        else:
            tile.setFill("blue")
            tile.type = "Player"

        current.setFill("white")
        current.type = "Floor"


def key_events(event):

    """Event handler for pressed keys"""

    current = get_current_tile()                # Get the current player tile
    x = current.x                               # Get the x-coordinate
    y = current.y                               # Get the y-coordinate

    if x > 0 and x < COLUMNS and y > 0 and y < ROWS:    # Check if it's possible to make a move_player within the boundaries of the map

        up = maze[x][y - 1]
        down = maze[x][y + 1]
        left = maze[x - 1][y]
        right = maze[x + 1][y]

        if event.keysym == "s":                 # If 's' is pressed, the bot solves the maze
            solve_maze(current, x, y)

        if event.keysym == "Up":                # If any of the arrow keys are pressed,
                                                # move_player accordingly
            move_player(up, current)

        if event.keysym == "Down":

            move_player(down, current)

        if event.keysym == "Left":

            move_player(left, current)

        if event.keysym == "Right":

            move_player(right, current)


def get_current_tile():

    """Returns the current player tile from maze"""

    for row in maze:
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
        [1, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]         # A hard-coded map

ROWS = 40
COLUMNS = 40
WINDOW_HEIGHT = 1000
WINDOW_BREADTH = 1000
TILE_SIZE = WINDOW_BREADTH / COLUMNS

w1 = GraphWin(
                "Maze",
                WINDOW_HEIGHT,   # Height of window
                WINDOW_BREADTH   # Breadth of window
)

maze = []           # Contains all tile objects that makes up the maze
open_list = []      # Contains all current possible paths to the exit
solution = []       # Stores the optimal solution to the exit


# =============================================
#                   MAIN
# =============================================

display_maze()         # Display the map with its initial conditions

while True:

    w1.bind("<Key>", key_events)               # Sends all key_events events to the event handler
    w1.bind("<Button-1>", callback)     # Sends all mouse events to the event handler, sets focus to the window
    w1.getMouse()                       # Prevents the window from closing, without this the program won't run properly
