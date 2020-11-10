import random
import pickle

class QLearning:
    def __init__(self, player=1, discount_rate=0.9, learning_rate=0.1, epsilon=0.3):
        self.player = player
        self.gamma = discount_rate
        self.alpha = learning_rate
        self.epsilon = epsilon
        self.epsilon_min = 0.01
        self.epsilon_decay = 5.8e-07
        self.q_table = dict()

    def get_actionPool(self, state):
        actionPool = []
        for index, square in enumerate(state):
            if square == "_":
                actionPool.append(index)
        return actionPool

    def action(self, state, exploration=True):
        actionPool = self.get_actionPool(state)
        if exploration is True and random.random() < self.epsilon:
            return random.choice(actionPool)
        best_action = None
        best_q_value = None
        for action in actionPool:
            q_value = self.q_table.get((tuple(state), action), 0)
            if best_q_value is None or q_value > best_q_value:
                best_q_value = q_value
                best_action = action
        return best_action
    
    def update_q_table(self, state, action, reward, next_state):
        old_value = self.q_table.get((tuple(state), action), 0)
        next_action = self.action(next_state, exploration=False)
        next_value = self.q_table.get((tuple(next_state), next_action), 0)
        self.q_table[(tuple(state), action)] = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_value)
        self.update_epsilon()

    def save_q_table(self):
        q = open("./codes/agent"+str(self.player)+"_q_table.pkl", "wb")
        pickle.dump(self.q_table, q)
        q.close()
        
    def load_q_table(self):
        q = open("./codes/agent"+str(self.player)+"_q_table.pkl", "rb")
        self.q_table = pickle.load(q)
        q.close()

    def update_epsilon(self):
        if self.epsilon >= self.epsilon_min:
            self.epsilon -= self.epsilon_decay
