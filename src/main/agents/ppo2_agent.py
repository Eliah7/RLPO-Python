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
import matplotlib .pyplot as plt
from src.main.env.environment import Environment

if __name__ == '__main__':
    # The algorithms require a vectorized environment to run
    env = DummyVecEnv([lambda: Environment(3000)])
    model = PPO2(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=20000)
    obs = env.reset()

    for i in range(2000):
      action, _states = model.predict(obs)
      obs, rewards, done, info = env.step(action)
      print(rewards)
      env.render()