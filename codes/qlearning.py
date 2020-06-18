# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

import numpy as np
import pandas as pd
import pickle
import random

class QLearning:
    def __init__(self, player=1):
        self.player = player
        self.opponent = 2 if player == 1 else 1
        self.state_names = self.set_states()
        self.states = 3**9
        self.actions = 9
        self.q_table = self.set_q_table()
        self.learning_rate = 0.1
        self.discount_rate = 0.9
        self.epsilon = 0.3
        
    def set_states(self):
        probabilities = ["0","1","2"]
        state_names = [q+w+e+r+t+y+u+i+o for q in probabilities for w in probabilities 
                       for e in probabilities for r in probabilities for t in probabilities 
                       for y in probabilities for u in probabilities for i in probabilities 
                       for o in probabilities]
        return state_names
    
    def set_q_table(self):
        q_table = np.zeros((self.states, self.actions))
        q_table = pd.DataFrame(q_table, index=self.state_names)
        return q_table
    
    def save_q_table(self):
        q = open("agent"+str(self.player)+"_q_table.pkl", "wb")
        pickle.dump(self.q_table, q)
        q.close()
        
    def load_q_table(self):
        q = open("agent"+str(self.player)+"_q_table.pkl", "rb")
        self.q_table = pickle.load(q)
        q.close()
        
    def board_to_state(self, state):
        state_rep = str()
        for square in state.reshape(-1,):
            if square == "_":
                state_rep += "0"
            elif square == "X":
                state_rep += "1"
            elif square == "O":
                state_rep += "2"
        return state_rep
    
    def get_actionPool(self, state):
        return list(np.where(state.reshape(9,) == "_")[0])
    
    def action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 8)
        state_rep = self.board_to_state(state)
        actionPool = self.get_actionPool(state)
        for action in np.array(np.argsort(self.q_table.loc[state_rep, :]))[::-1]:
            if action in actionPool:
                return action
        
    def update_q_table(self, state, action, reward, next_state):
        state_rep = self.board_to_state(state)
        if next_state is not None:
            next_state_rep = self.board_to_state(next_state)
            q_value = self.q_table.at[state_rep, action]
            next_q_value = np.max(self.q_table.loc[next_state_rep,:])
            new_q_value = (1 - self.learning_rate) * q_value + self.learning_rate * (reward + self.discount_rate * next_q_value)
            self.q_table.at[state_rep, action] = new_q_value
        elif next_state is None:
            q_value = self.q_table.at[state_rep, action]
            new_q_value = (1 - self.learning_rate) * q_value + self.learning_rate * reward
            self.q_table.at[state_rep, action] = new_q_value