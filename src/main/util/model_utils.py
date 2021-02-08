# Authored by elia on 27/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
import numpy as np
import pandas as pd

def evaluate(agent_model, num_episodes=10):
    """
    Evaluate a RL agent
    :param model: (BaseRLModel object) the RL Agent
    :param num_episodes: (int) number of episodes to evaluate it
    :return: (Tuple) Mean reward for the last num_episodes, list of all rewards
    """
    # This function will only work for a single Environment
    env = agent_model.get_env()
    all_episode_rewards = []
    max_action = []
    max_reward = -1000000000
    for i in range(num_episodes):
        episode_rewards = []
        done = False
        obs = env.reset()

        while not done:
            # _states are only useful when using LSTM policies

            action, _states = agent_model.predict(obs)
            # here, action, rewards and dones are arrays
            # because we are using vectorized env
            obs, reward, done, info = env.step(action)

            episode_rewards.append(reward[0])

            if reward[0] > max_reward:
                max_action = action
                max_reward = reward



        all_episode_rewards.append(sum(episode_rewards))

    print("BEST ACTION: {}".format(max_action))
    print("BEST REWARD: {}".format(max_reward))

    mean_episode_reward = np.mean(all_episode_rewards)
    print("Mean reward:", mean_episode_reward, "Num episodes:", num_episodes)

    return mean_episode_reward, all_episode_rewards

def run_ensemble(model, num_episodes=10):
    max_model_action = []
    max_model_reward = -100000000
    best_model = ""
    best_model_info = {}

    for model_name, agent_model in model.items():
        print("\n\n---------------------------------")
        print("---------------------------------")
        print("\t\t TRAINING {}".format(model_name))
        print("---------------------------------")
        print("---------------------------------")

        env = agent_model.get_env()

        all_episode_rewards = []
        max_action = []
        max_reward = -1000000000
        best_info = {}

        for i in range(num_episodes):
            episode_rewards = []
            done = False
            obs = env.reset()

            while not done:
                action, _states = agent_model.predict(obs)
                obs, reward, done, info = env.step(action)
                episode_rewards.append(reward[0])

                if reward[0] > max_reward:
                    max_action = action
                    max_reward = reward
                    best_info = info[0]

            all_episode_rewards.append(sum(episode_rewards))

        if max_reward > max_model_reward:
            max_model_action = max_action
            max_model_reward = max_reward
            best_model = model_name
            best_model_info = best_info

        mean_episode_reward = np.mean(all_episode_rewards)
        print("Mean reward:", mean_episode_reward, "Num episodes:", num_episodes)

    print("BEST MODEL: {}".format(best_model))
    print("BEST ACTION: {}".format(max_model_action))
    print("BEST REWARD: {}".format(max_model_reward))
    print("MIN VOL: {}".format(best_model_info["min"]))
    print("MAX VOL: {}".format(best_model_info["max"]))


def get_mva_kva(grid_name):
    model_desc = pd.read_csv("../env/data/models.csv")

    return float(model_desc.loc[model_desc['File'] == grid_name]['Mva']), float(model_desc.loc[model_desc['File'] == grid_name]['Kva'])

