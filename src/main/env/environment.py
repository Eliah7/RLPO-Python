# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
import gym
from gym import spaces
import numpy as np
from src.main.env.data import *
from src.main.util.binary_ops import *
from src.main.util.java_utils import dlf_analyse
from src.main.util.model_utils import *

class Environment(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    """
        Arguments:
            max_capacity: Total Available Power
            n_discrete_actions: Number of actions 
            line_data: Array of (index, from_node, to_node, R, X)
            load_data: Array of (node, p, q, bus_type, status, priority) 
    """
    def __init__(self, grid_name="bus33", line_data=lineData, load_data=loadData):
        super(Environment, self).__init__()

        self.grid_name = grid_name

        if not grid_name == "bus33":
            self.load_data, self.line_data = get_data_from_csv(grid_name)
        else:
            self.load_data = load_data
            self.line_data = line_data

        self.max_capacity, _ = get_mva_kva(grid_name) # MVa to KVa
        self.max_capacity = self.max_capacity * 1000
        self.n_nodes = len(self.line_data) + 1

        self.reward_range = spaces.Box(low=0, high=1000, shape=(1,)) #spaces.Box(np.array(0), np.array(100))

        high = np.array([np.inf] * self.n_nodes)
        self.observation_space = spaces.Box(-high, high)

        self.action_space = spaces.Discrete(self.n_nodes+1)
        self.num_actions = 0

        # (sum_power_assigned, sum_status, sum_priority) : defines state
        #  implement value-function approximation to summarize node information
        # self.observation_space = spaces.Box(np.array((-10000, -10000, -10000)), np.array((10000, 10000, 10000)))

        self.done = False

    def get_remaining_power(self, max_capacity, load_data):
        power_assigned = np.sum(load_data[:, 1] * load_data[:, 4])
        return max_capacity - power_assigned

    def step(self, action):
        # Execute one time step within the environment

        obs = self.get_observation(action)
        reward = self.reward()

        power_values_from_dlf, _ = dlf_analyse(self.line_data, self.load_data, grid_name=self.grid_name)

        if self.num_actions == 10:
            # print("DONE")
            self.done = True
        else:
            self.done = False
            self.num_actions += 1

        self.done = True
        return obs, reward, self.done, {}

    def reset(self):
        # Reset the state of the environment to an initial state
        if not self.grid_name == "bus33":
            self.load_data, self.line_data = get_data_from_csv(self.grid_name)
        else:
            self.load_data = loadData
            self.line_data = lineData

        self.num_actions = 0

        self.done = False

        return self.get_observation()

    def get_observation(self, action=np.inf):
        if action == np.inf :
            return self.current_state()
        else:
            if action <= self.n_nodes:
                self.act_from_num(action=action)
            else:
                action_str = get_bin_str_with_max_count(action, self.n_nodes)
                self.act(action_str)
            # print("CURRENT STATE: " + str(self.load_data[:, 4]))

            return self.current_state()

    def act_from_num(self, action):
        if action == 0:
            pass
        elif self.load_data[:, 4][action-1] == 0:
            self.load_data[:, 4][action-1] = 1
        else:
            self.load_data[:, 4][action-1] = 0

    def act(self, action_str):
        for action in range(len(action_str)):
            self.load_data[:, 4][action] = int(action_str[action])

        self.load_data[:, 4][0] = 1
        return

    def current_state(self):
        power_assigned = np.sum(self.load_data[:, 1] * self.load_data[:, 4])
        sum_statuses = np.sum(self.load_data[:, 4])
        sum_priorities = np.sum(self.load_data[:, 5])

        return np.array(self.load_data[:, 1] * self.load_data[:, 4] * np.square(self.load_data[:, 5]))

    def reward(self):
        status_reward = np.sum(self.load_data[:, 1] * self.load_data[:, 4] * np.square(self.load_data[:, 5])) ** 0.4 # positive rewards
        power_assigned = 1 - np.sum(self.load_data[:, 1] * self.load_data[:, 4])  ** 0.4

        power_values_from_dlf, _ = dlf_analyse(self.line_data, self.load_data, grid_name=self.grid_name)

        power_values_from_dlf = np.array(power_values_from_dlf)
        # print(power_values_from_dlf)

        if not ((power_values_from_dlf.min() > 0.9 and power_values_from_dlf.max() < 1.1)):
            print("values of max and min outside range")
            return -90000000000

        return status_reward / self.n_nodes

    def power_assigned(self):
        return np.sum(self.load_data[:, 1] * self.load_data[:, 4])