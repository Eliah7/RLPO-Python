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

if __name__ == '__main__':
    env = DummyVecEnv([lambda: Environment(1000)])
    # env = Monitor(env, "./logs")
    model = PPO2(MlpPolicy, env, verbose=1)

    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - PPO2")

    model.learn(total_timesteps=20000)

    # evaluate after training
    _, all_rewards = evaluate(model)

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - PPO2")