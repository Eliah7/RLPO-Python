# Authored by elia on 27/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
import numpy as np
import pandas as pd

<<<<<<< HEAD
def evaluate(agent_model, num_episodes=1):
=======
def evaluate(agent_model, num_episodes=10):
>>>>>>> 6033157baaa0c3c976aaf55286970513ba1fe0d5
    """
    Evaluate a RL agent
    :param model: (BaseRLModel object) the RL Agent
    :param num_episodes: (int) number of episodes to evaluate it
    :return: (Tuple) Mean reward for the last num_episodes, list of all rewards
    """
    # This function will only work for a single Environment
    env = agent_model.get_env()
    all_episode_rewards = []
    for i in range(num_episodes):
        episode_rewards = []
        done = False
        obs = env.reset()
        max_action = []
        max_reward = -1000000000
        while not done:
            # _states are only useful when using LSTM policies

            action, _states = agent_model.predict(obs)
            # here, action, rewards and dones are arrays
            # because we are using vectorized env
            obs, reward, done, info = env.step(action)

            episode_rewards.append(reward)

            if(reward > max_reward):
                max_action = action
                max_reward = reward

        print("BEST ACTION: {}".format(max_action))
        print("BEST REWARD: {}".format(max_reward))


        all_episode_rewards.append(sum(episode_rewards))

    mean_episode_reward = np.mean(all_episode_rewards)
    print("Mean reward:", mean_episode_reward, "Num episodes:", num_episodes)

    return mean_episode_reward, all_episode_rewards

def get_mva_kva(grid_name):
    model_desc = pd.read_csv("../env/data/models.csv")

    return float(model_desc.loc[model_desc['File'] == grid_name]['Mva']), float(model_desc.loc[model_desc['File'] == grid_name]['Kva'])

