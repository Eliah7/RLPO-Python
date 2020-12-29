# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN, A2C
from src.main.env.environment import Environment
from src.main.util.graph_utils import *
from src.main.util.model_utils import *
import os

import time

def train_dqn(grid_name):
    log_dir = "./tensorboard/"
    os.makedirs(log_dir, exist_ok=True)

    env = Environment(grid_name=grid_name)

    # env = Monitor(env, "./logs")
    model = DQN(MlpPolicy, env=env, _init_setup_model=True, verbose=1, exploration_fraction=0.1,
                tensorboard_log=log_dir)
    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - DQN")

    start = time.time()
    model.learn(total_timesteps=2000)
    end = time.time()
    print("Training Time: {}".format(end - start))

    model.save("./saved_models/dqn")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - DQN")


if __name__ == '__main__':
    log_dir = "./tensorboard/"
    os.makedirs(log_dir, exist_ok=True)

    grid_name = "bbq-village"
    env = Environment(grid_name=grid_name)

    # env = Monitor(env, "./logs")
    model = DQN(MlpPolicy,env=env, _init_setup_model=True, verbose=1, exploration_fraction=0.1, tensorboard_log=log_dir)
    # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - DQN")

    start = time.time()
    model.learn(total_timesteps=2000)
    end = time.time()
    print("Training Time: {}".format(end - start))

    model.save("./saved_models/dqn")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - DQN")