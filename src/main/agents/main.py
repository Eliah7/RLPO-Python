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
import click

def train_all_agents(agent, grid_name, train_steps, state_type):
    print("Training Steps: {}".format(train_steps))
    print("Training ... ")

    env = DummyVecEnv([lambda: Environment(grid_name=grid_name, action_type=state_type)])

    env = VecCheckNan(env, raise_exception=True)

    if agent == "a2c":
        if train_steps == 0:
            train_a2c(env)
        else:
            train_a2c(env, grid_name, train_steps=train_steps)
    elif agent == "dqn":
        if train_steps == 0:
            train_dqn(env)
        else:
            train_dqn(env, grid_name, train_steps=train_steps)
    elif agent == "ppo2":
        if train_steps == 0:
            train_ppo2(env)
        else:
            train_ppo2(env, grid_name, train_steps=train_steps)

    print(
        "Training Done. Run tensorboard --logdir <directory of tensorboard> to see training curves. \nPlots are in the plots directory")


if __name__ == '__main__':
    np.seterr(all='raise')
    agent = input(click.style("Enter the name of the agent: (eg. a2c, dqn, ppo2)>", "red", bold=True))

    grid_name = input(click.style("Enter the electrical grid to use: (eg. kimweri, bbq-village, bus33, abiudi, solar)>", "red", bold=True))

    train_steps = int(input(click.style("Enter the number of training steps: (0 for default)>", "red", bold=True)))

    state_type =input(click.style("Enter the type of state: (discrete or continous)>", "red", bold=True)).lower()
    state_type = "discrete" if state_type == "" else state_type

    print("Training Steps: {}".format(train_steps))
    print("Training ... ")

    train_all_agents(agent, grid_name,train_steps, state_type)