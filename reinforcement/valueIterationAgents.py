# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        neg_inf = float("-inf")
        # loop for all iterations
        for i in range(self.iterations):       
            # init list of nxt_values for this iteration        
            nxt_values = util.Counter()
            # for each state in the grid
            for state in self.mdp.getStates():
                # init max_value var to neg inf
                max_Qvalue = neg_inf
                # loop for all available actions
                for action in self.mdp.getPossibleActions(state):
                    Qvalue = self.getQValue(state, action)
                    # if nxt Qvalue is greater than max Qvalue
                    if Qvalue > max_Qvalue:
                        # update max Qvalue
                        max_Qvalue = Qvalue

                # if maxQvalue is not neg inf
                if max_Qvalue != neg_inf:
                    # store new max Qvalue in dict of nxt values
                    nxt_values[state] = max_Qvalue
            
            # update values
            self.values = nxt_values


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        
        # get list of surrounding states and their probabilities
        trans_states_probs = self.mdp.getTransitionStatesAndProbs(state, action)
        # init next Qvalue
        Qvalue = 0
        # for each surrounding state
        for trans_state_prob in trans_states_probs:
            # calculate next value using bellman equation 
            # sum(Prob*(Reward+(Discount*PrevValue)))
            Qvalue += trans_state_prob[1] * (self.mdp.getReward(state, action, trans_state_prob[0]) + self.discount * self.values[trans_state_prob[0]])

        # return nxt Qvalue
        return Qvalue


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        # init max Qvalue/Action vars to neg inf and null
        neg_inf = float("-inf")
        max_Qvalue = neg_inf
        # returning None if there are no actins available
        max_Qvalue_Action = None
        
        # loop for all available actions
        for action in self.mdp.getPossibleActions(state):
            # obtain next Qvalue for given action
            Qvalue = self.getQValue(state, action)
            # if nxt Qvalue is greater than max Qvalue
            if Qvalue > max_Qvalue:
                # update max Qvalue and action
                max_Qvalue = Qvalue
                max_Qvalue_Action = action

        # return action for max Qvalue
        return max_Qvalue_Action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
