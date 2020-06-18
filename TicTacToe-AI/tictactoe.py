# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

import numpy as np

class TicTacToe:
    def __init__(self):
        self.turn = 1
        self.player1_marker = "X"
        self.player2_marker = "O"
        self.state = np.full((3,3), '_', dtype=str)
        self.winner = None
        self.action_list = list(range(9))
    
    def reset(self):
        self.turn = 1
        self.state = np.full((3,3), '_')
        self.winner = None
    
    def render(self):
        print(self.state)
        
    def decode_action(self, action):
        column = action // 3
        row = action % 3
        return column, row
        
    def isValid(self, column, row):
        if column < 0 or column > 2 or row < 0 or row > 2:
            return False
        if self.state[column, row] == "_":
            return True
        return False
    
    def step(self, action):
        column, row = self.decode_action(action)
        if self.isValid(column, row):   
            if self.turn == 1:
                self.state[column, row] = self.player1_marker
            elif self.turn == 2:
                self.state[column, row] = self.player2_marker
            done = self.check_winner()
            self.turn = 1 if self.turn == 2 else 2
            return done
        return
        
    def check_winner(self):
        if self.turn == 1:
            if self.state[0,0] == self.state[1,1] == self.state[2,2] == self.player1_marker:
                self.winner = self.player1_marker
                return True
            elif self.state[0,2] == self.state[1,1] == self.state[2,0] == self.player1_marker:
                self.winner = self.player1_marker
                return True
            for index in range(3):
                if self.state[index,0] == self.state[index,1] == self.state[index,2] == self.player1_marker:
                    self.winner = self.player1_marker
                    return True
                elif self.state[0,index] == self.state[1,index] == self.state[2,index] == self.player1_marker:
                    self.winner = self.player1_marker
                    return True
        elif self.turn == 2:
            if self.state[0,0] == self.state[1,1] == self.state[2,2] == self.player2_marker:
                self.winner = self.player2_marker
                return True
            elif self.state[0,2] == self.state[1,1] == self.state[2,0] == self.player2_marker:
                self.winner = self.player2_marker
                return True
            for index in range(3):
                if self.state[index,0] == self.state[index,1] == self.state[index,2] == self.player2_marker:
                    self.winner = self.player2_marker
                    return True
                elif self.state[0,index] == self.state[1,index] == self.state[2,index] == self.player2_marker:
                    self.winner = self.player2_marker
                    return True
        if np.sum(self.state == "_") == 0:
            self.winner = "Tie"
            return True
        return False