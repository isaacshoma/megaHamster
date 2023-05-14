from roboid import *

hamster = HamsterS()

# intializing list and dictionaries to store coordinates and direction
front = "N"
current_position = [0, 0]
explored = set()
neighbors = []
pure_wall = []
record = ""

# Define the maze as a 2D array of dictionaries
maze = [
    [
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
    ],
    [
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
    ],
    [
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
    ],
    [
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
    ],
    [
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
        {'S': 0, 'E': 0, 'W': 0, 'N': 0, "passed": 0},
    ],

]


# checking left side
def left(frontCheck=True):
    global front
    hamster.turn_left(90, 80)
    if frontCheck:
        if front == "N":
            front = "W"
        elif front == "S":
            front = "E"
        elif front == "W":
            front = "S"
        elif front == "E":
            front = "N"


# checking right side
def right(frontCheck=True):
    global front
    hamster.turn_right(90, 80)
    if frontCheck:
        if front == "N":
            front = "E"
        elif front == "S":
            front = "W"
        elif front == "W":
            front = "N"
        elif front == "E":
            front = "S"


# calibrating the hamster to ceentre its self after every cell
def calibration():
    global front
    global pure_wall
    backwall = 0
    print(front)

    if front == "N":
        if 'S' in pure_wall:
            backwall = 1
            print("S WALL")

    if front == "W":
        if 'E' in pure_wall:
            backwall = 1
            print("E WALL")

    if front == "E":
        if 'W' in pure_wall:
            backwall = 1
            print("W WALL")

    if front == "S":
        if 'N' in pure_wall:
            backwall = 1
            print("N WALL")

    if backwall == 1:
        hamster.move_backward(4, 40)
        hamster.move_forward(2, 80)

# moving foward will constantly updated the following global varibles
def forwards():
    global maze
    global current_position
    global record
    global neighbors
    global pure_wall
    print(f"pure_wall {pure_wall}")
    print(f"passChange pos {current_position}")
    calibration()
    maze[current_position[0]][current_position[1]]["passed"] = 1
    print(maze[current_position[0]][current_position[1]])
    hamster.move_forward(9, 80)
    if front == "N":
        current_position[1] += 1
        if len(neighbors) > 1:
            record += "1"
        record += "N"

    elif front == "S":
        current_position[1] -= 1
        if len(neighbors) > 1:
            record += "1"
        record += "S"

    elif front == "E":
        current_position[0] += 1
        if len(neighbors) > 1:
            record += "1"
        record += "E"

    elif front == "W":
        current_position[0] -= 1
        if len(neighbors) > 1:
            record += "1"
        record += "W"


def uturn(frontCheck=True):
    global front
    hamster.turn_left(180)
    if frontCheck:
        if front == "N":
            front = "S"
        elif front == "S":
            front = "N"
        elif front == "W":
            front = "E"
        elif front == "E":
            front = "W"


# Movements for the hamster
def turntoWfromN():
    left()


def turntoEfromN():
    right()


def turntoNfromW():
    right()


def turntoNfromE():
    left()


def turntoSfromE():
    right()


def turntoSfromW():
    left()


def turntoEfromS():
    left()


def turntoWfromS():
    right()


def turntoNfromS():
    uturn()


def turntoSfromN():
    uturn()


def turntoWfromE():
    uturn()


def turntoEfromW():
    uturn()


# dead end check function that will grab the current position of the hamster
# and it will count how many walls that one cell has
# if it has more than 3 walls, it is a dead end
def dead_end_check():
    global maze, current_position, front
    count = 0
    print(current_position[0], current_position[1])
    for i in maze[current_position[0]][current_position[1]].values():
        if i == 1:
            count += 1
    if maze[current_position[0]][current_position[1]]["passed"] == 1:
        count -= 1
    if count == 4:
        return True
    return False


# Function to get the current position in the maze
# constantly updates from the update_maze function
def get_position_in_maze():
    """
    Returns the current position of the hamster in the maze.
    """
    global current_position
    return current_position


# once the hamster searches the cell, it detects the neighbours of what sides are open or closed
# 1 meaning there is a wall, 0 meaning it is open
def get_neighbors():
    global maze
    global current_position
    global neighbors
    global pure_wall
    neighbors = []
    mapsize = len(maze)
    if maze[current_position[0]][current_position[1]]["N"] == 0:
        if -1 < (current_position[1] + 1) < mapsize:
            if (current_position[0], current_position[1] + 1) not in explored:
                neighbors.append("N")

    if maze[current_position[0]][current_position[1]]["W"] == 0:
        if -1 < (current_position[0] - 1) < mapsize:
            if (current_position[0] - 1, current_position[1]) not in explored:
                neighbors.append("W")

    if maze[current_position[0]][current_position[1]]["E"] == 0:
        if -1 < (current_position[0] + 1) < mapsize:
            if (current_position[0] + 1, current_position[1]) not in explored:
                neighbors.append("E")

    if maze[current_position[0]][current_position[1]]["S"] == 0:
        if -1 < (current_position[1] - 1) < mapsize:
            if (current_position[0], current_position[1] - 1) not in explored:
                neighbors.append("S")

    if "N" not in neighbors:
        maze[current_position[0]][current_position[1]]["N"] = 1

    if "W" not in neighbors:
        maze[current_position[0]][current_position[1]]["W"] = 1

    if "E" not in neighbors:
        maze[current_position[0]][current_position[1]]["E"] = 1

    if "S" not in neighbors:
        maze[current_position[0]][current_position[1]]["S"] = 1

    return neighbors


# Function to update the maze with a wall at the current position
# basic structure of a depth_first_search, using the stack method
# i append the direction to the front of the queue
def update_maze(direction):
    """
    Updates the maze dictionary with a wall at the current position.
    """
    global maze, current_position, front, neighbors, pure_wall

    if direction == 'f':
        maze[current_position[0]][current_position[1]][front] = 1
        pure_wall.append(front)

    if direction == 'l':
        if front == 'N':
            maze[current_position[0]][current_position[1]]['W'] = 1
            pure_wall.append('W')
        if front == 'W':
            maze[current_position[0]][current_position[1]]['S'] = 1
            pure_wall.append('S')
        if front == 'S':
            maze[current_position[0]][current_position[1]]['E'] = 1
            pure_wall.append('E')
        if front == 'E':
            maze[current_position[0]][current_position[1]]['N'] = 1
            pure_wall.append('N')

    if direction == 'b':
        if front == 'N':
            maze[current_position[0]][current_position[1]]['S'] = 1
            pure_wall.append('S')
        if front == 'W':
            maze[current_position[0]][current_position[1]]['E'] = 1
            pure_wall.append('E')
        if front == 'S':
            maze[current_position[0]][current_position[1]]['N'] = 1
            pure_wall.append('N')
        if front == 'E':
            maze[current_position[0]][current_position[1]]['W'] = 1
            pure_wall.append('W')

    if direction == 'r':
        if front == 'N':
            maze[current_position[0]][current_position[1]]['E'] = 1
            pure_wall.append('E')
        if front == 'E':
            maze[current_position[0]][current_position[1]]['S'] = 1
            pure_wall.append('S')
        if front == 'S':
            maze[current_position[0]][current_position[1]]['W'] = 1
            pure_wall.append('W')
        if front == 'W':
            maze[current_position[0]][current_position[1]]['N'] = 1
            pure_wall.append('N')


# Move forward through the maze until the end is reached
# this is the basics movements it is making while it is updating the maze
while True:
    # check goal
    goal = [2, 2]
    if current_position == goal:
        wait(3000)
        print("MADE IT")

    neighbors = []
    pure_wall = []
    print(current_position)
    left_side = hamster.left_proximity()
    print(f"front: {left_side}")
    if left_side > 60:
        update_maze('f')
    wait(20)
    right_side = hamster.right_proximity()
    print(f"Right: {right_side}")
    if right_side > 35:
        update_maze('r')
    left(False)
    wait(20)

    left_side = hamster.left_proximity()
    print(f"Left: {left_side}")
    if left_side > 60:
        update_maze('l')

    left(False)
    wait(20)
    left_side = hamster.left_proximity()
    print(f"Back: {left_side}")
    if left_side > 60:
        update_maze('b')

    uturn(False)
    explored.add(tuple(current_position))

    # The hamsters movements once its enters a dead end
    # It will start back tracking
    if dead_end_check():
        print("DEAD END")
        num = record.rfind("1")
        path = record[num + 1:]
        record = record[:num]
        print(path[::-1])
        print(num)
        print(record)
        wait(50)
        uturn()
        for i in path[::-1]:
            if i == "N":
                if front == "N":
                    turntoSfromN()
                    forwards()
                elif front == "E":
                    turntoSfromE()
                    forwards()
                elif front == "W":
                    turntoSfromW()
                    forwards()
                elif front == "S":
                    forwards()
            if i == "W":
                if front == "W":
                    turntoEfromW()
                    forwards()
                elif front == "N":
                    turntoEfromN()
                    forwards()
                elif front == "E":
                    forwards()
                elif front == "S":
                    turntoEfromS()
                    forwards()
            if i == "E":
                if front == "E":
                    turntoWfromE()
                    forwards()
                elif front == "N":
                    turntoWfromN()
                    forwards()
                elif front == "S":
                    turntoWfromS()
                    forwards()
                elif front == "W":
                    forwards()
            if i == "S":
                if front == "S":
                    turntoNfromS()
                    forwards()
                elif front == "N":
                    forwards()
                elif front == "E":
                    turntoNfromE()
                    forwards()
                elif front == "W":
                    turntoNfromW()
                    forwards()

    else:
        goto = ""
        for key, value in maze[current_position[0]][current_position[1]].items():
            if value == 0:
                goto = key
                break

        if front == 'N':
            if goto == 'E':
                turntoEfromN()
            elif goto == 'W':
                turntoWfromN()
            elif goto == 'S':
                turntoSfromN()

        if front == 'E':
            if goto == 'N':
                turntoNfromE()
            elif goto == 'W':
                turntoWfromE()
            elif goto == 'S':
                turntoSfromE()

        if front == 'W':
            if goto == 'N':
                turntoNfromW()
            elif goto == 'E':
                turntoEfromW()
            elif goto == 'S':
                turntoSfromW()

        if front == 'S':
            if goto == 'N':
                turntoNfromS()
            elif goto == 'E':
                turntoEfromS()
            elif goto == 'W':
                turntoWfromS()

        if front == goto:
            forwards()
    print(maze[current_position[0]][current_position[1]])
    print(record)
    print()
    wait(20)
