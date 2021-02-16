# Authored by elia on 30/12/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

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
from main.util.graph_utils import *
from main.util.model_utils import *
from main.env.environment import Environment
from stable_baselines.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise, AdaptiveParamNoiseSpec
from stable_baselines import DDPG

import time

def train_ddpg(grid_name, train_steps=20000):
    log_dir = "./tensorboard/"
    env = Environment(grid_name=grid_name)
    # env = Monitor(env, "./logs")
    param_noise = None
    n_actions = env.n_nodes
    action_noise = OrnsteinUhlenbeckActionNoise(mean=np.zeros(n_actions), sigma=float(0.5) * np.ones(n_actions))
    model = DDPG(MlpPolicy, env, verbose=1, param_noise=param_noise, action_noise=action_noise)

    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - DDPG")

    start = time.time()
    model.learn(total_timesteps=train_steps)
    end = time.time()
    print("Training Time: {}".format(end - start))
    model.save("./saved_models/ddpg")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - DDPG")

if __name__ == '__main__':
    log_dir = "./tensorboard/"

    env = Environment()
    param_noise = None
    n_actions = env.n_nodes
    action_noise = OrnsteinUhlenbeckActionNoise(mean=np.zeros(n_actions), sigma=float(0.5) * np.ones(n_actions))
    model = DDPG(MlpPolicy, env, verbose=1, param_noise=param_noise, action_noise=action_noise)

    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - DDPG")

    start = time.time()
    model.learn(total_timesteps=2000)
    end = time.time()
    print("Training Time: {}".format(end - start))
    model.save("./saved_models/ddpg")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - DDPG")