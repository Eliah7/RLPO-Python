# Authored by elia on 11/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
from stable_baselines import DQN, A2C, PPO2
from src.main.util.model_utils import evaluate

if __name__ == '__main__':
    # model = A2C.load("./saved_models/a2c")
    model = DQN.load("./saved_models/dqn")
    # model = PPO2.load("./saved_models/ppo2")
    evaluate(model)