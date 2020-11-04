# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy, CnnPolicy
# from stable_baselines.common.policies import MlpPolicy
from stable_baselines import DQN, A2C
from src.main.env.environment import Environment
from stable_baselines.bench import Monitor
import numpy as np
from src.main.util.graph_utils import *
from src.main.util.model_utils import *


if __name__ == '__main__':
    env = DummyVecEnv([lambda: Environment(15)])
    # env = Monitor(env, "./logs")
    model = DQN(MlpPolicy, env, verbose=1)

    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - DQN")

    model.learn(total_timesteps=20000)

    # evaluate after training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - DQN")