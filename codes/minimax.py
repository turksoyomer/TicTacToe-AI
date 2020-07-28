# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

import random

class MiniMax:
    def __init__(self, player=1):
        self.player = player
        self.opponent = 1 if player == 2 else 2
        self.player1_marker = "X"
        self.player2_marker = "O"
        self.name = "MiniMax"
    
    def evaluate(self, state, done, winner):
        if done and winner == self.player:
            return 1
        elif done and winner == self.opponent:
            return -1
        else:
            return 0
        
    def get_actionPool(self, state):
        actionPool = []
        for index, square in enumerate(state):
            if square == "_":
                actionPool.append(index)
        return actionPool

    def check_winner(self, state, turn):
        if turn == 1:
            if state[0] == state[4] == state[8] == self.player1_marker:
                winner = 1
                return True, winner
            elif state[2] == state[4] == state[6] == self.player1_marker:
                winner = 1
                return True, winner
            for i in range(0, 9, 3):
                if state[i+0] == state[i+1] == state[i+2] == self.player1_marker:
                    winner = 1
                    return True, winner
            for j in range(3):
                if state[j+0] == state[j+3] == state[j+6] == self.player1_marker:
                    winner = 1
                    return True, winner
        elif turn == 2:
            if state[0] == state[4] == state[8] == self.player2_marker:
                winner = 2
                return True, winner
            elif state[2] == state[4] == state[6] == self.player2_marker:
                winner = 2
                return True, winner
            for i in range(0, 9, 3):
                if state[i+0] == state[i+1] == state[i+2] == self.player2_marker:
                    winner = 2
                    return True, winner
            for j in range(3):
                if state[j+0] == state[j+3] == state[j+6] == self.player2_marker:
                    winner = 2
                    return True, winner
        if state.count("_") == 0:
            winner = "Tie"
            return True, winner
        return False, None
    
    def step(self, state, action, turn):
        if turn == 1:
            state[action] = self.player1_marker
        elif turn == 2:
            state[action] = self.player2_marker
        done, winner = self.check_winner(state, turn)
        return state, done, winner
    
    def action(self, state):
        """minimax-search"""
        _, action = self.max_value(state, done=False, winner=None)
        return action
    
    def max_value(self, state, done, winner):
        if done:
            return self.evaluate(state, done, winner), None
        best_action = None
        best_value = -float("inf")
        actionPool = self.get_actionPool(state)
        random.shuffle(actionPool)
        for action in actionPool:
            next_state, done, winner = self.step(state.copy(), action, self.player)
            value, _ = self.min_value(next_state, done, winner)
            if value > best_value:
                best_action = action
                best_value = value
        return best_value, best_action
    
    def min_value(self, state, done, winner):
        if done:
            return self.evaluate(state, done, winner), None
        best_action = None
        best_value = float("inf")
        actionPool = self.get_actionPool(state)
        random.shuffle(actionPool)
        for action in actionPool:
            next_state, done, winner = self.step(state.copy(), action, self.opponent)
            value, _ = self.max_value(next_state, done, winner)
            if value < best_value:
                best_action = action
                best_value = value
        return best_value, best_action