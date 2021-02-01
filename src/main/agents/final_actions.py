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
import time
import click

if __name__ == '__main__':
    grid_name = input(click.style("Enter grid name>", "red", bold=True))

    learning_rate = input(click.style("Enter learning rate>", "red", bold=True))

    gamma = input(click.style("Enter gamma>", "red", bold=True))

    env = DummyVecEnv([lambda: Environment(grid_name=grid_name, action_type="continous")])
    env = VecCheckNan(env, raise_exception=True)

    model_no = int(input(click.style("Enter model to test: {1 => dqn, 2 => ppo, 3 => a2c}>", "red", bold=True)))

    if model_no == 1:
        model: DQN = DQN.load("./saved_models/dqn_{}_learning_rate{}_gamma{}".format(grid_name, learning_rate, gamma), env=env)
    elif model_no == 2:
        model: PPO2 = PPO2.load("./saved_models/ppo2_{}_learning_rate{}_gamma{}".format(grid_name, learning_rate, gamma), env=env)
    elif model_no == 3:
        model: A2C = A2C.load("./saved_models/a2c_{}_learning_rate{}_gamma{}".format(grid_name, learning_rate, gamma), env=env)
    else:
        raise Exception('Choose valid model')

    # model: A2C = A2C.load("./saved_models/a2c", env=env)
    # model: PPO2 = PPO2.load("./saved_models/ppo2", env=env)
    # model: DQN = DQN.load("./saved_models/dqn", env=env)

    start = time.time()
    evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 10))
    # print(all_rewards)