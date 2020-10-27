# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
import gym
from gym import spaces
import numpy as np
from .data import *
from src.main.util.binary_ops import *


class Environment(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    N_DISCRETE_ACTIONS = len(lineData)

    """
        Arguments:
            max_capacity: Total Available Power
            n_discrete_actions: Number of actions 
            line_data: Array of (index, from_node, to_node, R, X)
            load_data: Array of (node, p, q, bus_type, status, priority) 
    """
    def __init__(self, max_capacity, n_nodes=N_DISCRETE_ACTIONS, line_data=lineData, load_data=loadData):
        super(Environment, self).__init__()

        self.max_capacity = max_capacity
        self.n_nodes = n_nodes
        self.load_data = load_data
        self.line_data = line_data
        self.max_action = get_max_number(self.n_nodes)
        self.reward_range = spaces.Box(low=0, high=1000, shape=(1,)) #spaces.Box(np.array(0), np.array(100))
        self.action_space = spaces.Discrete(self.n_nodes)

        # (sum_power_assigned, sum_status, sum_priority) : defines state
        #  implement value-function approximation to summarize node information
        self.observation_space = spaces.Box(np.array((-max_capacity, -max_capacity, -max_capacity)), np.array((max_capacity, max_capacity, max_capacity)))

        self.done = False

    def get_remaining_power(self, max_capacity, load_data):
        power_assigned = np.sum(load_data[:, 1] * load_data[:, 4])

        return max_capacity - power_assigned

    def step(self, action):
        # Execute one time step within the environment
        obs = self.get_observation(action)
        reward = self.reward()

        self.done = True

        # if self.get_remaining_power(self.max_capacity, self.load_data) > 0 :
        #     self.done = True
        # elif self.power_assigned() > self.max_capacity:
        #     self.done = True
        # else:
        #     self.done = False

        return obs, reward, True, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        self.load_data = loadData
        self.line_data = lineData
        # self.remain_power = self.get_remaining_power(self.max_capacity, self.load_data)
        # self.power_assigned = np.sum(self.load_data[:, 1] * self.load_data[:, 4])
        self.done = False

        return self.get_observation()

    def get_observation(self, action=np.inf):
        # print(action)
        # assert (2 ** self.n_nodes) >= action >= 0, 'Action can not exceed nodes count'

        if action == np.inf :
            return self.current_state()
        else:
            # print("===> Action : {} in binary: {}".format(action, get_bin_str_with_max_count(action, self.n_nodes)))
            action_str = get_bin_str_with_max_count(action, self.n_nodes)

            self.act(action_str)

            return self.current_state()


    def act(self, action_str):

        
        for action in range(self.n_nodes):
            self.load_data[:, 4][action] = int(action_str[action])

    def current_state(self):
        power_assigned = np.sum(self.load_data[:, 1] * self.load_data[:, 4])
        sum_statuses = np.sum(self.load_data[:, 4])
        sum_priorities = np.sum(self.load_data[:, 5])

        return np.array([power_assigned, sum_statuses, sum_priorities])

    def reward(self):
        status_reward = 1 - np.sum(self.load_data[:, 4] * self.load_data[:, 5]) ** 0.4 # positive rewards
        power_assigned = 1 - np.sum(self.load_data[:, 1] * self.load_data[:, 4])  ** 0.4

        return status_reward * power_assigned

    def power_assigned(self):
        return np.sum(self.load_data[:, 1] * self.load_data[:, 4])