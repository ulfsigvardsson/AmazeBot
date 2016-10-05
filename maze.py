from tile import *

def has_neigbour_floor(list, x, y):
    """Determines if a tile has neighbouring floors, to be used for maze generation"""
    neighbourlist=neighbour_list(list, x, y)
    for neighbour in neighbourlist:
        if neighbour.type == "Floor":
            return True
        #TODO: connect to a maze generating function

def neighbour_list(list, x, y):
    """Returns a list of all neighbouring tiles in four directions"""
    neighbours = [list[x][y + 1], list[x][y - 1], list[x + 1][y], list[x - 1][y]]
    return neighbours

def findpath(tile, x, y):
    """Moves the 'player' through the maze

       tile:: Tile-object representing the current position
       x:: integer, x-coordinates of 'tile'
       y:: integer, y-coordinates of 'tile'    """

    if tile.type == "Exit":
        tile.setFill("green")
        print "Success!"
        w1.getMouse()   # Keeps the window from closing
        quit()

    else:
        time.sleep(0.03)    # Time delay to enable visual tracking
        tile.setFill("yellow")
        tile.set_status("Visited")
        neighbours = neighbour_list(row_list, x, y)     # Finds all neighbouring tiles and returns them in a list

        neighbours.sort(key=lambda x: x.distance)   # Sorts the list of neighbours by distance to goal

        for neighbour in neighbours:    # Runs the findpath() function on all neighbours that is not a wall or have already been visited
            if neighbour.status != "Visited" and neighbour.type != "Wall":
                findpath(neighbour, neighbour.get_x(), neighbour.get_y())

def generate_map(tile, x, y):
    """Moves the 'player' through the maze

       tile:: Tile-object representing the current position
       x:: integer, x-coordinates of 'tile'
       y:: integer, y-coordinates of 'tile'    """

    if tile.type == "Exit":
        tile.setFill("green")
        print "Success!"
        w1.getMouse()   # Keeps the window from closing
        quit()

    else:
        time.sleep(0.03)    # Time delay to enable visual tracking
        tile.setFill("white")
        tile.set_type("Floor")
        neighbours = neighbour_list(row_list, x, y)     # Finds all neighbouring tiles and returns them in a list

        neighbours.sort(key=lambda x: x.distance)   # Sorts the list of neighbours by distance to goal

        for neighbour in neighbours:    # Runs the findpath() function on all neighbours that is not a wall or have already been visited
            if neighbour.status != "Visited" and neighbour.type != "Wall":
                findpath(neighbour, neighbour.get_x(), neighbour.get_y())


def make_goal(tile):
    """Establishes a goal tile

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
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 3, 1, 0, 0, 1, 1, 0, 1],
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
goal = None
start = None


for i in range(len(map)): # Outer loop for generating every row
    column_list = []  # List set to empty for a iteration of a new row

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

findpath(start, start.get_x(), start.get_y())
w1.getMouse()


