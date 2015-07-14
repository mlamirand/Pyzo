import math
import random

def categorical_draw(probs):
  z = random.random()
  cum_prob = 0.0
  for i in range(len(probs)):
    prob = probs[i]
    cum_prob += prob
    if cum_prob > z:
      return i
  
  return len(probs) - 1

class Softmax:
  def __init__(self, temperature, counts, Qk):
    self.temperature = temperature
    self.counts = counts
    self.Qk = Qk
    return
  
  def initialize(self, n_arms):
    self.counts = [0 for col in range(n_arms)]
    self.Qk = [0.0 for col in range(n_arms)]
    return
  
  def select_arm(self):
    z = sum([math.exp(v / self.temperature) for v in self.Qk])
    probs = [math.exp(v / self.temperature) / z for v in self.Qk]
    return categorical_draw(probs)

  def update(self, chosen_arm, reward):
    self.counts[chosen_arm] += 1
    n = self.counts[chosen_arm]
    
    Qk = self.Qk[chosen_arm]
    new_Qk = Qk + (1 /n) * (reward - Qk)
    self.Qk[chosen_arm] = new_Qk
    return

def main():
  
    players = [Softmax(0.1, [], []) for i in range(2000)]
    for j in range(0, 2000):
        players[j].initialize(10)
    
    averages = []
    for i in range(0, 1000):
        rewards = []
        for player in players:
            arm = player.select_arm()
            reward = np.random.normal(player.Qk[arm], 1)
            player.update(arm, reward)
            rewards.append(reward)
        averages.append(np.sum(rewards)/2000)
        
    x = np.arange(0, 1000, 1)
    y = np.array(averages)
    plt.scatter(x, y, color = (0, 0.8, 0.9))
  
  
main()