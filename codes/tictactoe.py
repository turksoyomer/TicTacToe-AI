# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

class TicTacToe:
    def __init__(self):
        self.turn = 1
        self.player1_marker = "X"
        self.player2_marker = "O"
        self.state = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.winner = None
        self.action_list = list(range(9))
    
    def reset(self):
        self.turn = 1
        self.state = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.winner = None
    
    def render(self):
        print("\n%s %s %s\n%s %s %s\n%s %s %s\n" % tuple(self.state))

    def isValid(self, action):
        if not 0 <= action <= 8:
            return False
        if self.state[action] == "_":
            return True
        return False
    
    def step(self, action):
        if self.isValid(action):   
            if self.turn == 1:
                self.state[action] = self.player1_marker
            elif self.turn == 2:
                self.state[action] = self.player2_marker
            done = self.check_winner()
            self.turn = 1 if self.turn == 2 else 2
            return done
        return
        
    def check_winner(self):
        if self.turn == 1:
            if self.state[0] == self.state[4] == self.state[8] == self.player1_marker:
                self.winner = self.player1_marker
                return True
            elif self.state[2] == self.state[4] == self.state[6] == self.player1_marker:
                self.winner = self.player1_marker
                return True
            for i in range(0, 9, 3):
                if self.state[i+0] == self.state[i+1] == self.state[i+2] == self.player1_marker:
                    self.winner = self.player1_marker
                    return True
            for j in range(3):
                if self.state[j+0] == self.state[j+3] == self.state[j+6] == self.player1_marker:
                    self.winner = self.player1_marker
                    return True
        elif self.turn == 2:
            if self.state[0] == self.state[4] == self.state[8] == self.player2_marker:
                self.winner = self.player2_marker
                return True
            elif self.state[2] == self.state[4] == self.state[6] == self.player2_marker:
                self.winner = self.player2_marker
                return True
            for i in range(0, 9, 3):
                if self.state[i+0] == self.state[i+1] == self.state[i+2] == self.player2_marker:
                    self.winner = self.player2_marker
                    return True
            for j in range(3):
                if self.state[j+0] == self.state[j+3] == self.state[j+6] == self.player2_marker:
                    self.winner = self.player2_marker
                    return True
        if self.state.count("_") == 0:
            self.winner = "Tie"
            return True
        return False