# Authored by elia on 27/10/2020

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

import matplotlib.pyplot as plt
import numpy as np

def plot_moving_avg(totalrewards, title="Running Average for an Actor-Critic Agent"):
    N = len(totalrewards)
    running_avg = np.empty(N)
    for t in range(N):
        running_avg[t] = totalrewards[max(0, t-100):(t+1)].mean()
    plt.plot(running_avg)
    plt.title(title)
    plt.xlabel("Timestep")
    plt.ylabel("Average Running Reward")
    plt.savefig("./plots/{}".format(title))
    plt.show()
