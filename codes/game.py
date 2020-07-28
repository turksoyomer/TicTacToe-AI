# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

from tictactoe import TicTacToe
from minimax import MiniMax
from alphabeta import AlphaBeta
from qlearning import QLearning
import time

game = TicTacToe()
user = int(input("Player1(X) or Player2(O):"))
ai = 2 if user == 1 else 1
ai_algorithm = input("""Choose your opponent:
                     1. MiniMax Algorithm
                     2. MiniMax with Alpha-Beta Pruning
                     3. Q-Learning Agent
                     """)

if ai_algorithm == "1":
    agent = MiniMax(player=ai)
elif ai_algorithm == "2":
    agent = AlphaBeta(player=ai)
elif ai_algorithm == "3":
    agent = QLearning(player=ai)
    agent.epsilon = 0
    agent.load_q_table()
    
while True:
    game.render()
    print("-----------------------------------------------------------------")
    if game.turn == user:
        action = int(input("Action (0-8):"))
        done = game.step(action)
        if done:
            game.render()
            break
    elif game.turn == ai:
        a = time.time()
        action = agent.action(game.state)
        b = time.time()
        print("%s Algorithm - Calculation Time: %.2f seconds" % (agent.name, b-a))
        done = game.step(action)
        if done:
            game.render()
            break
print("winner:", game.winner)
