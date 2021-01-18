# Authored by elia on 11/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
from stable_baselines import DQN, A2C, PPO2
from src.main.util.model_utils import evaluate
from src.main.env.environment import Environment
from stable_baselines.common.vec_env import DummyVecEnv, VecCheckNan

if __name__ == '__main__':
    env = DummyVecEnv([lambda: Environment(grid_name="bus33", action_type="continous")])
    env = VecCheckNan(env, raise_exception=True)

    model = A2C.load("./saved_models/a2c", env=env)

    evaluate(model)