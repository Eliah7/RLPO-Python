# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""



from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy, CnnPolicy
from stable_baselines import DQN, A2C
from src.main.env.environment import Environment
from stable_baselines.bench import Monitor
import gym
from gym import spaces
import numpy as np

if __name__ == '__main__':
    env = DummyVecEnv([lambda: Environment(3000)])
    # env = Monitor(env, "./logs")
    model = A2C(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=25000)

    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        print(rewards)