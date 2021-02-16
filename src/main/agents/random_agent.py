# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

import gym
from main.env.environment import Environment
from main.util.model_utils import *

if __name__ == '__main__':
    env = Environment(15)

    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            print("EPISODE: {} REWARD: {}".format(i_episode, reward))