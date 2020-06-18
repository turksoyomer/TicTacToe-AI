# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

from tictactoe import TicTacToe
from qlearning import QLearning
from alphabeta import AlphaBeta

game = TicTacToe()
agent1 = QLearning(player=1)
agent1.epsilon=0
agent1.load_q_table()
agent2 = AlphaBeta(player=2)

score_board = {"Agent1":0, "AlphaBeta":0, "Tie":0}

for e in range(100):   
    game.reset()
    while True:
        if game.turn == 1:
            action = agent1.action(game.state)
            done = game.step(action)
            if done:
                break
        elif game.turn == 2:
            action = agent2.action(game.state)
            done = game.step(action)
            if done:
                break
    if game.winner == "X":
        score_board["Agent1"] += 1
    elif game.winner == "O":
        score_board["AlphaBeta"] += 1
    elif game.winner == "Tie":
        score_board["Tie"] += 1
        
#%%
        
game = TicTacToe()
agent1 = AlphaBeta(player=1)
agent2 = QLearning(player=2)
agent2.epsilon=0
agent2.load_q_table()

score_board = {"Agent2":0, "AlphaBeta":0, "Tie":0}

for e in range(100):   
    game.reset()
    while True:
        if game.turn == 1:
            action = agent1.action(game.state)
            done = game.step(action)
            if done:
                break
        elif game.turn == 2:
            action = agent2.action(game.state)
            done = game.step(action)
            if done:
                break
    if game.winner == "X":
        game.render()
        score_board["AlphaBeta"] += 1
    elif game.winner == "O":
        score_board["Agent2"] += 1
    elif game.winner == "Tie":
        score_board["Tie"] += 1