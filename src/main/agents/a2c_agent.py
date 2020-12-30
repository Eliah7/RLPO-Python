# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""



# from stable_baselines.common.vec_env import DummyVecEnv
# from stable_baselines.deepq.policies import MlpPolicy, CnnPolicy
from stable_baselines.common.policies import MlpPolicy
from stable_baselines import DQN, A2C
from src.main.env.environment import Environment
# from stable_baselines.bench import Monitor
# import numpy as np
from src.main.util.graph_utils import *
from src.main.util.model_utils import *

import time

def train_a2c(grid_name, train_steps=1000):
    log_dir = "./tensorboard/"

    env = Environment(grid_name=grid_name)
    # # env = Monitor(env, "./logs")
    model = A2C(MlpPolicy, env=env, _init_setup_model=False, verbose=1, tensorboard_log=log_dir)
    model.setup_model()

    # # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - A2C")

    start = time.time()
    model.learn(total_timesteps=train_steps)
    end = time.time()
    print("Training Time: {}".format(end - start))
    # model.save("./saved_models/a2c")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))
    # print(all_rewards)

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training")

if __name__ == '__main__':
    log_dir = "./tensorboard/"

    env = Environment()
    # # env = Monitor(env, "./logs")
    model = A2C(MlpPolicy,env=env, _init_setup_model=False, verbose=1, tensorboard_log=log_dir )
    model.setup_model()


    # # evaluate before training
    _, all_rewards = evaluate(model)
    plot_moving_avg(np.array(all_rewards), title="Running Average reward before training - A2C")

    start = time.time()
    model.learn(total_timesteps=2000)
    end = time.time()
    print("Training Time: {}".format(end - start))
    # model.save("./saved_models/a2c")

    # evaluate after training
    start = time.time()
    _, all_rewards = evaluate(model)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))
    # print(all_rewards)

    plot_moving_avg(np.array(all_rewards), title="Running Average reward after training - A2C")