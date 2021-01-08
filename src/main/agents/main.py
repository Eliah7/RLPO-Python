# Authored by elia on 29/12/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from src.main.agents.a2c_agent import train_a2c
from src.main.agents.dqn_agent import train_dqn
from src.main.agents.ppo2_agent import train_ppo2
from stable_baselines.common.vec_env import DummyVecEnv, VecCheckNan
from src.main.env.environment import Environment
import numpy as np

if __name__ == '__main__':
    np.seterr(all='raise')
    print("Enter the name of the agent: (eg. a2c, dqn, ppo2)")
    agent = input()
    print("Agent: {}".format(agent))

    print("Enter the electrical grid to use: (eg. kimweri, bbq-village, bus33, abiudi, solar)")
    grid_name = input()
    print("Grid: {}".format(grid_name))

    print("Enter the number of training steps: (0 for default)")
    train_steps = int(input())

    print("Enter the type of state: (discrete or continous)")
    state_type = input().lower()
    state_type = "discrete" if state_type == "" else state_type

    # print("Enter the load shedding percentage: ")
    # load_shedding = int(input())

    print("Training Steps: {}".format(train_steps))
    print("Training ... ")

    env = DummyVecEnv([lambda: Environment(grid_name=grid_name, action_type=state_type)])
    #env = Environment(grid_name=grid_name, action_type=state_type)
    env = VecCheckNan(env, raise_exception=True)

    if agent == "a2c":
        if train_steps == 0:
            train_a2c(env)
        else:
            train_a2c(env, train_steps=train_steps)
    elif agent == "dqn":
        if train_steps == 0:
            train_dqn(env)
        else:
            train_dqn(env, train_steps=train_steps)
    elif agent == "ppo2":
        if train_steps == 0:
            train_ppo2(env)
        else:
            train_ppo2(env, train_steps=train_steps)
    # elif agent == "ddpg":
    #     if train_steps == 0:
    #         train_ddpg(grid_name)
    #     else:
    #         train_ddpg(grid_name, train_steps=train_steps)

    print("Training Done. Run tensorboard --logdir <directory of tensorboard> to see training curves. \nPlots are in the plots directory")

