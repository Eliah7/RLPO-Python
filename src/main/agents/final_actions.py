# Authored by elia on 11/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
from stable_baselines import DQN, A2C, PPO2
from src.main.util.model_utils import evaluate
from src.main.env.environment import Environment

if __name__ == '__main__':
    env = Environment(100)
    # model = A2C.load("./saved_models/a2c")
    model = DQN.load("./saved_models/dqn", env=env)
    # model.env = env
    # model = PPO2.load("./saved_models/ppo2")
    evaluate(model)