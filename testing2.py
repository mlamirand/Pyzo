import numpy as np
import random
import matplotlib.pyplot as plt
import time

def reward(x1, x2, x3):
    noise = np.random.normal(0, 1)
    y = x1 + x2 - 0.5 * x3 + noise
    
    if y < 2 or y > 5:
        prob = 0
    else:
        prob = 1
        
    z = random.random()
    if z < prob:
        return 1
    else:
        return 0
    
def main():
    
    for i in range(100):
        print(reward(2, 2, 2))
        
main()