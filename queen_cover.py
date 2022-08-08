#######################################################################################
## Specification of Queen Cover problem for coursework 1,(Spring 2021)
#######################################################################################

## "deepcopy" is used to make a copy of a state and then change
## it to create a new state.
## This is needed because of the way Python handles lists.
## If you just assign a list to a new variable then you will
## just get a new pointer to the same list.

from copy import deepcopy

#######################################################################################
## Make the function to print out problem info
## This has to return a function with no parameters as the search procedure
## requires this

## Information of the board Size:

def make_qc_problem_info(board_height, board_width):
    def qc_problem_info():
        print("The Queen Cover Problem\n",
              "Board Size: ", board_height, " height x ", board_width, " wide")

    return qc_problem_info

#######################################################################################
## Description of state:

## The state is an  array where entries are 2 (for a queen), 1 (for covered)
## and 0 (for uncovered) where n = board_size.

## Specify the initial state:
## This function will set all initial states to zero
def qc_initial_state(board_height, board_width):
    return [[0 for j in range(board_width)] for i in range(board_height)]

#######################################################################################
##  Define the possible actions:

## an action is a pair of indices (i,j) to place a queen


## When is each action possible?

def lfn(listin, target):
    ans = []
    for i in range(len(listin)):
        if listin[i] == target:
            ans.append(i)
    return ans

## This function will find the action (or index(i,j)) of specific state
def findwhere(listoflists, target):
    result = []
    for row in range(len(listoflists)):
        rowresult = lfn(listoflists[row], target)
        rowpairs = [[row, rowresult[i]] for i in range(len(rowresult))]
        result.extend(rowpairs)
    return result

## This function will return a list of possible actions (or indices (i,j)) to place a queen
def qc_possible_actions(state):
    uncovered = findwhere(state, 0)
    covered = findwhere(state, 1)
    uncovered.extend(covered)
    return uncovered


def number_queens(state):
    number = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 2:
                number += 1
    return number


def rows_used(state):
    number = 0
    for i in range(len(state)):
        rowtotal = 0
        for j in range(len(state[0])):
            if state[i][j] == 2:
                rowtotal += 1
        if rowtotal > 0:
            number += 1
    return number


def cols_used(state):
    number = 0
    for j in range(len(state[0])):
        coltotal = 0
        for i in range(len(state)):
            if state[i][j] == 2:
                coltotal += 1
        if coltotal > 0:
            number += 1
    return number


def number_uncovered(state):
    number = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                number += 1
    return number
#######################################################################################
## The successor state function:

## This function will return the allocated new state after taking action.
## Please be noted the state is an  array where entries are 2 (for a queen), 1 (for covered)
## and 0 (for uncovered) where n = board_size.
def qc_successor_state(action, state):
    newstate = deepcopy(state)
    # TODO: Implement me:
    ## Implement a double 'for loop' and
    ## check whether the action covers which indices(i,j).
    for i in range(len(state)):
        for j in range(len(state[i])):
            if newstate[i][j] == 0:
                if covers(action,(i,j),state):
                    newstate[i][j] = 1 
                else:
                    newstate [i][j] == 2
    return newstate

## This function will return True where action covers the place,
## otherwise will return 'False'.
def covers(action, place, state):
    if action[0] == place[0]:
        return True
    elif action[1] == place[1]:
        return True
    elif action[0] - place[0] == action[1] - place[1]:
        return True
    elif action[0] - place[0] == place[1] - action[1]:
        return True
    else:
        return False
#######################################################################################
## test for goal:
def qc_test_goal_state(state):
    # TODO: Implement me
    if number_uncovered(state) != 0:
        return False
    else:
        return True
#######################################################################################
## problem specification:

def make_qc_problem(board_height, board_width):
    return (None,
            make_qc_problem_info(board_height, board_width),
            qc_initial_state(board_height, board_width),
            qc_possible_actions,
            qc_successor_state,
            qc_test_goal_state
            )


