# Authored by elia on 11/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
from stable_baselines import DQN, A2C, PPO2
from src.main.util.model_utils import evaluate
from src.main.env.environment import Environment


def test_rl_agent(agent, environment):
    pass


if __name__ == '__main__':
    env = Environment(grid_name="bus33")
    # model = A2C.load("./saved_models/a2c")
    model = DQN.load("./saved_models/dqn", env=env)

    obs = env.reset()
    print("INPUTS: {}".format(obs))
    done = False

    while not done:
        action, _states = model.predict(obs)
        next_obs, reward, done, info = env.step(action)

    if done:

        print("OUPUT: {}".format(next_obs))
        print("REWARD: {}".format(reward))
