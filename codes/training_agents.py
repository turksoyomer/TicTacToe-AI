# -*- coding: utf-8 -*-
"""
@author: turksoyomer
"""

from tictactoe import TicTacToe
from qlearning import QLearning

game = TicTacToe()
agent1 = QLearning(player=1)
agent2 = QLearning(player=2)

agent1_memory = [None, None, None, None]
agent2_memory = [None, None, None, None]

for e in range(500000):
    game.reset()
    while True:
        if game.turn == 1:
            state1 = game.state.copy()
            agent1_memory[0] = state1
            action1 = agent1.action(state1)
            agent1_memory[1] = action1
            agent1_memory[2] = 0
            done1 = game.step(action1)
            next_state1 = game.state.copy()
            agent2_memory[3] = next_state1
            if done1:
                if game.winner == "X":
                    agent1_memory[2] = 1
                    agent2_memory[2] = -1
                elif game.winner == "O":
                    agent1_memory[2] = -1    
                    agent2_memory[2] = 1
                agent1.update_q_table(agent1_memory[0], agent1_memory[1], agent1_memory[2], None)
                agent2.update_q_table(agent2_memory[0], agent2_memory[1], agent2_memory[2], None)
                break
            if agent2_memory[0] is not None:
                agent2.update_q_table(agent2_memory[0], agent2_memory[1], agent2_memory[2], agent2_memory[3])
        elif game.turn == 2:
            state2 = game.state.copy()
            agent2_memory[0] = state2
            action2 = agent2.action(state2)
            agent2_memory[1] = action2
            agent2_memory[2] = 0
            done2 = game.step(action2)
            next_state2 = game.state.copy()
            agent1_memory[3] = next_state2
            if done2:
                if game.winner == "X":
                    agent1_memory[2] = 1
                    agent2_memory[2] = -1
                elif game.winner == "O":
                    agent1_memory[2] = -1    
                    agent2_memory[2] = 1
                agent1.update_q_table(agent1_memory[0], agent1_memory[1], agent1_memory[2], None)
                agent2.update_q_table(agent2_memory[0], agent2_memory[1], agent2_memory[2], None)
                break
            if agent1_memory[0] is not None:
                agent1.update_q_table(agent1_memory[0], agent1_memory[1], agent1_memory[2], agent1_memory[3])
    if e % 100 == 0:
        print("Episode", e, "completed")
print("Training completed")