import numpy as np
import random
import matplotlib.pyplot as plt

def reward(x1, x2, x3):
    noise = np.random.normal(0, 1)
    y = x1 + x2 - 0.5 * x3 + noise
    
    if y < 5 or y > 7:
        prob = 0
    else:
        prob = 0.5
        
    z = random.random()
    if z < prob:
        return 1
    else:
        return 0
    
class brain:
    def __init__(self, x1, x2, x3, values, chosen, epsilon):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.values = [[[0 for k in range(11)] for j in range(11)] for i in range(11)]
        self.chosen = [[[0 for k in range(11)] for j in range(11)] for i in range(11)]
        self.epsilon = epsilon
        
    def choose_xs(self):
        if np.random.random() > self.epsilon:
            n = np.argmax(self.values)
            [x, y, z] = np.unravel_index([n], (11, 11, 11))
            x1 = x[0]
            x2 = y[0]
            x3 = z[0]
            return [x1, x2, x3]
        else:
            x1 = random.randint(0, 10)
            x2 = random.randint(0, 10)
            x3 = random.randint(0, 10)
            return [x1, x2, x3]
            
    def update(self):
        [x1, x2, x3] = self.choose_xs()
        r = reward(x1, x2, x3)
        
        self.chosen[x1][x2][x3] += 1
        n = self.chosen[x1][x2][x3]
        self.values[x1][x2][x3] = self.values[x1][x2][x3] + (1/n) * (r - self.values[x1][x2][x3])
        
        return r


def main():
    
    tests = [brain(0, 0, 0, [], [], 0.1) for i in range(1000)]
    
    averages = []
    for i in range(0, 2000):
        rewards = []
        for test in tests:
            reward = test.update()
            rewards.append(reward)
        averages.append(np.sum(rewards)/1000)
        

    x = np.arange(0, 2000, 1)
    y = np.array(averages)
    plt.scatter(x, y, color = (0.9, 0, 0))
    
main()
    