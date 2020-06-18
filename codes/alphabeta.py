# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

import numpy as np
import random

class AlphaBeta:
    def __init__(self, player=1):
        self.player = player
        self.opponent = 1 if player == 2 else 2
        self.player1_marker = "X"
        self.player2_marker = "O"
    
    def evaluate(self, state, done, winner):
        if done and winner == self.player:
            return 1
        elif done and winner == self.opponent:
            return -1
        else:
            return 0
        
    def get_actionPool(self, state):
        return list(np.where(state.reshape(9,) == "_")[0])
    
    def decode_action(self, action):
        column = action // 3
        row = action % 3
        return column, row
    
    def check_winner(self, state, turn):
        if turn == 1:
            if state[0,0] == state[1,1] == state[2,2] == self.player1_marker:
                winner = 1
                return True, winner
            elif state[0,2] == state[1,1] == state[2,0] == self.player1_marker:
                winner = 1
                return True, winner
            for index in range(3):
                if state[index,0] == state[index,1] == state[index,2] == self.player1_marker:
                    winner = 1
                    return True, winner
                elif state[0,index] == state[1,index] == state[2,index] == self.player1_marker:
                    winner = 1
                    return True, winner
        elif turn == 2:
            if state[0,0] == state[1,1] == state[2,2] == self.player2_marker:
                winner = 2
                return True, winner
            elif state[0,2] == state[1,1] == state[2,0] == self.player2_marker:
                winner = 2
                return True, winner
            for index in range(3):
                if state[index,0] == state[index,1] == state[index,2] == self.player2_marker:
                    winner = 2
                    return True, winner
                elif state[0,index] == state[1,index] == state[2,index] == self.player2_marker:
                    winner = 2
                    return True, winner
        if np.sum(state == "_") == 0:
            winner = "Tie"
            return True, winner
        return False, None
    
    def step(self, state, action, turn):
        column, row = self.decode_action(action)
        if turn == 1:
            state[column, row] = self.player1_marker
        elif turn == 2:
            state[column, row] = self.player2_marker
        done, winner = self.check_winner(state, turn)
        return state, done, winner
    
    def action(self, state):
        """alpha-beta-search"""
        value, action = self.max_value(state, alpha=-float("inf"), beta=float("inf"), done=False, winner=None)
        return action
    
    def max_value(self, state, alpha, beta, done, winner):
        if done:
            return self.evaluate(state, done, winner), None
        best_action = None
        best_value = -float("inf")
        actionPool = self.get_actionPool(state)
        random.shuffle(actionPool)
        for action in actionPool:
            next_state, done, winner = self.step(state.copy(), action, self.player)
            value, _ = self.min_value(next_state, alpha, beta, done, winner)
            if value > best_value:
                best_value = value
                best_action = action
            if value >= beta:
                return best_value, best_action
            alpha = max(alpha, value)
        return best_value, best_action
            
    def min_value(self, state, alpha, beta, done, winner):
        if done:
            return self.evaluate(state, done, winner), None
        best_action = None
        best_value = float("inf")
        actionPool = self.get_actionPool(state)
        random.shuffle(actionPool)
        for action in actionPool:
            next_state,done, winner = self.step(state.copy(), action, self.opponent)
            value, _ = self.max_value(next_state, alpha, beta, done, winner)
            if value < best_value:
                best_action = action
                best_value = value
            if value <= alpha:
                return best_value, best_action
            beta = min(beta, value)
        return best_value, best_action