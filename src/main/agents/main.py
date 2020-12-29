# Authored by elia on 29/12/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from src.main.agents.a2c_agent import train_a2c
from src.main.agents.dqn_agent import train_dqn
from src.main.agents.ppo2_agent import train_ppo2

if __name__ == '__main__':
    print("Enter the name of the agent: (eg. a2c, dqn, ppo2)")
    agent = input()
    print("Agent: {}".format(agent))

    print("Enter the electrical grid to use: (eg. kimweri, bbq-village, bus33, abiudi, solar)")
    grid_name = input()
    print("Grid: {}".format(grid_name))

    print("Training ... ")

    if agent == "a2c":
        train_a2c(grid_name)
    elif agent == "dqn":
        train_dqn(grid_name)
    elif agent == "ppo2":
        train_ppo2(grid_name)

    print("Training Done. Run tensorboard --logdir <directory of tensorboard> to see training curves. \nPlots are in the plots directory")

