# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():

    # Makes an array the same size a grid to check off.
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid[1]))]
    # Assigns the starting square as checked.
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    # Flags stop the program when it finds the goal or exhausts options.
    found = False  # Flag that is set when search is complete
    resign = False  # Flag that is set if we can't expand

    while not found and not resign:

        # Checks to see if we still have an element on the open list
        if len(open) == 0:
            resign = True
            print "We failed"

        else:
            # remove node from list, backwards sort then pop off end element.
            open.sort()
            open.reverse()
            next = open.pop()

            # Our expantion
            x = next[1]
            y = next[2]
            g = next[0]

            # Check to see if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                print next # successful goal

            else:
                # expand winning element and add to new open list.
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1



print search()

