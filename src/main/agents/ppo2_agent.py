# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

import gym
import json
import datetime as dt
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
from src.main.util.graph_utils import *
from src.main.util.model_utils import *
from src.main.env.environment import Environment

import time

def train_ppo2(env, train_steps=20000):
    log_dir = "./tensorboard/"
    # env = Monitor(env, "./logs")
    model = PPO2(MlpPolicy, env=env, _init_setup_model=True, verbose=1, tensorboard_log=log_dir)

    # evaluate before training
    # _, all_rewards = evaluate(model)
    # plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - PPO2")

    start = time.time()
    model.learn(total_timesteps=train_steps)
    end = time.time()
    print("Training Time: {}".format(end - start))
    model.save("./saved_models/ppo2")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - PPO2")

if __name__ == '__main__':
    log_dir = "./tensorboard/"
    env = DummyVecEnv([lambda: Environment()])
    # env = Monitor(env, "./logs")
    model = PPO2(MlpPolicy, env=env, _init_setup_model=True, verbose=1, tensorboard_log=log_dir)

    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - PPO2")

    start = time.time()
    model.learn(total_timesteps=2000)
    end = time.time()
    print("Training Time: {}".format(end - start))
    model.save("./saved_models/ppo2")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - PPO2")