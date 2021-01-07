# Authored by elia on 11/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
from stable_baselines import DQN, A2C, PPO2
from src.main.util.model_utils import evaluate
from src.main.env.environment import Environment
import time


def test_rl_agent(agent, environment):
    pass


if __name__ == '__main__':
    env = Environment(grid_name="bus33")
    # model = A2C.load("./saved_models/a2c")
    model = DQN.load("./saved_models/dqn", env=env)

    obs = env.reset()
    print("INPUTS: {}".format(obs))
    done = False

    start = time.time()
    _, all_rewards = evaluate(model, num_episodes=100)
    end = time.time()
    print("Running time per time step: {}".format((end - start) / 100))

    # print("OUTPUT: {}".format(next_obs))
    # print("REWARD: {}".format(reward))
