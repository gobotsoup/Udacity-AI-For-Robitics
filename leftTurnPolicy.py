# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

init = [4, 3, 0] # first 2 elements are coordinates, third is direction
action = [-1, 0, 1] #right turn, no turn, left turn
action_name = ['R', '#', 'L']
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    direction = init[2]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    policy2D[x][y] = "*"
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True 
                elif grid[x][y] == 0:
                    v2 = []
                    for a in range(len(action)):
                        f = forward[(direction + action[a]) % 3]
                        #print "f=%s a=%s" % (f, action[a])
                        x2 = x + f[0]
                        y2 = y + f[1]                        
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            spot = [value[x2][y2] + cost[a], action_name[a], a]
                            v2.append(spot)
                    v2.sort()                    
                    if v2[0][0] < value[x][y]:
                        #policy2D[x][y] = forward_name[a]
                        #print "dir=%s cost=%d" % (v2[0][1], v2[0][0])
                        policy2D[x][y] = v2[0][1]
			direction = v2[0][2]
                        change = True
                        value[x][y] = v2[0][0]
    for i in range(len(policy2D)):
        print policy2D[i]
    
    return policy2D # Make sure your function returns the expected grid.

optimum_policy2D()
