# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # A stack data structure is used search the deepest nodes first
    next_node_stack = Stack()  # Stack to store next node to visit
    next_path_stack = Stack()  # Stack to store next path
    visited = []               # list to contain node that have been visited
    dfs_path = []              # list to contain the dfs path sequence

    # set current state to start state
    current_state = problem.getStartState()    
    
    # iterate until the goal state is reached
    while not problem.isGoalState(current_state):
        # if the current state has not been visited 
        if current_state not in visited:
            # add current state to list of visited nodes
            visited.append(current_state)
            # iterate through all neighouring nodes
            for neighour in problem.getSuccessors(current_state):
                # neighbour has not been visited
                if(neighour[0] not in visited):  
                    # push neighbour node and path list to top of stack
                    next_node_stack.push(neighour[0])
                    next_path_stack.push([dfs_path+[neighour[1]]])
        
        # to go deep first we pop next node and path from top of stack
        current_state = next_node_stack.pop()
        dfs_path = next_path_stack.pop()[0]

    return dfs_path


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # A queue data structure is used search the deepest nodes first
    next_node_queue = Queue()  # Queue to store next node to visit
    next_path_queue = Queue()  # Queue to store next path
    visited = []               # list to contain node that have been visited
    bfs_path = []              # list to contain the bfs path sequence

    # set current state to start state
    current_state = problem.getStartState()    
    
    # iterate until the goal state is reached
    while not problem.isGoalState(current_state):
        # if the current state has not been visited 
        if current_state not in visited:
            # add current state to list of visited nodes
            visited.append(current_state)
            # iterate through all neighouring nodes
            for neighour in problem.getSuccessors(current_state):
                # neighbour has not been visited
                if(neighour[0] not in visited):  
                    # push neighbour node and path list to top of queue
                    next_node_queue.push(neighour[0])
                    next_path_queue.push([bfs_path+[neighour[1]]])
        
        # to go deep first we pop next node and path from top of queue
        current_state = next_node_queue.pop()
        bfs_path = next_path_queue.pop()[0]

    return bfs_path
  

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # A queue data structure is used search the deepest nodes first
    next_node_queue = PriorityQueue()  # Queue to store next node to visit
    next_path_queue = PriorityQueue()  # Queue to store next path
    visited = []               # list to contain node that have been visited
    ucs_path = []              # list to contain the bfs path sequence

    # set current state to start state
    current_state = problem.getStartState()    
    
    # iterate until the goal state is reached
    while not problem.isGoalState(current_state):
        # if the current state has not been visited 
        if current_state not in visited:
            # add current state to list of visited nodes
            visited.append(current_state)
            # iterate through all neighouring nodes
            for neighbour in problem.getSuccessors(current_state):
                # neighbour has not been visited
                if(neighbour[0] not in visited):  
                    cost = problem.getCostOfActions(ucs_path+[neighbour[1]])
                    # push neighbour node and path list to top of stack
                    next_node_queue.push(neighbour[0], cost)
                    next_path_queue.push([ucs_path+[neighbour[1]]], cost)
        
        # to go deep first we pop next node and path from top of stack
        current_state = next_node_queue.pop()
        ucs_path = next_path_queue.pop()[0]

    return ucs_path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
