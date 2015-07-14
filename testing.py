import numpy as np
import matplotlib.pyplot as plt
import math
import random

class eGreedy:
    def __init__(self, epsilon, counts, Qk):
        self.epsilon = epsilon
        self.counts = counts
        self.Qk = Qk
        
    def initialize(self, n_arms):
        self.counts = [0 for col in range(n_arms)]
        self.Qk = [0 for col in range(n_arms)]
        return
        
    def choose_arm(self):
        #returns an arm for testing
        if np.random.random() > self.epsilon:
            #eploit
            return np.argmax(self.Qk)   #returns index of largest Qt(a)
        else:
            #explore
            return np.random.randint(len(self.Qk))    #returns random arm
    
    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        
        Qk = self.Qk[chosen_arm]
        new_Qk = Qk + (1 /n) * (reward - Qk)
        self.Qk[chosen_arm] = new_Qk
        return
        
def main():
    players = [eGreedy(0.1, [], []) for i in range(2000)]
    for j in range(0, 2000):
        players[j].initialize(10)
    
    averages = []
    for i in range(0, 1000):
        rewards = []
        for player in players:
            arm = player.choose_arm()
            reward = np.random.normal(player.Qk[arm], 1)
            player.update(arm, reward)
            rewards.append(reward)
        averages.append(np.sum(rewards)/2000)
        
    x = np.arange(0, 1000, 1)
    y = np.array(averages)
    plt.scatter(x, y, color = (0.75, 0, 1.0))
  
  
main()