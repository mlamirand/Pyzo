import numpy as np
import random
import matplotlib.pyplot as plt


def reward(a1, a2, a3):
    noise = np.random.normal(0, 1)
    y = a1 + a2 - a3 + noise
    
    if y < 2 or y > 5:
        prob = 0
    else:
        prob = 0.5
        
    z = random.random()
    if z < prob:
        return 1
    else:
        return 0
        
        
def generate_values():
    combos = []
    for i in range(11):
        for j in range(11):
            for k in range(11):
                s = (i, j, k)
                combos.append(s)
                
    y_vals = []
    for s in combos:
        noise = np.random.normal(0, 1)
        y = s[0] + s[1] - s[2] + noise
        y_vals.append(y)
    
    return (combos, y_vals)
    
def find_indices(y_vals):
    
    indices = []
    for i in range(len(y_vals)):
        if y_vals[i] > 2 and y_vals[i] < 5:
            indices.append(i)
            
    return indices

def find_best_xs():
    
    combos, y_vals = generate_values()
    
    indices = find_indices(y_vals)
    x_value_triplets = []
    for index in indices:
        x_value_triplets.append(combos[index])
    return x_value_triplets
    
    
def choose_triplet():
    triplets = find_best_xs()
    triplet = random.choice(triplets)
    return triplet

            
    
def main():
    
    
main()
    