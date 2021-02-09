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

np.seterr(all='raise')


class Environment(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    """
        Arguments:
            grid_name: string (name of the electrical grid)
    
            action_type: string ("continous" or "discrete")
    """

    def __init__(self, grid_name="bus33", action_type="discrete", load_shedding=100):
        super(Environment, self).__init__()

        self.grid_name = grid_name
        self.action_type = action_type

        # self.load_shedding = load_shedding

        self.load_data, self.line_data = get_data_from_csv(grid_name)

        self.max_capacity, _ = get_mva_kva(self.grid_name)  # MVa to KVa
        self.max_capacity = self.max_capacity * 1000
        self.n_nodes = len(self.line_data) + 1
        self.current_reward = self.calculate_reward(self.load_data[:, 3], self.load_data[:, 1], self.load_data[:, 4], self.load_data)

        self.reward_range = spaces.Box(low=0, high=1000, shape=(1,))  # spaces.Box(np.array(0), np.array(100))

        high = np.array([10000] * self.n_nodes)
        self.observation_space = spaces.Box(-high, high)

        if action_type.lower() == "discrete":
            self.action_space = spaces.Discrete(self.n_nodes + 1)
        elif action_type.lower() == "continous":
            # self.action_space = spaces.Box(low=0,high=1, shape=(self.n_nodes, 1), dtype=np.int)
            self.action_space = spaces.MultiBinary(self.n_nodes)
        else:
            raise Exception("Action type: {} not implemented. Use 'discrete' or 'continous'")

        self.num_actions = 0

        self.done = True

    def get_remaining_power(self):
        power_assigned = np.sum(self.load_data[:, 1] * self.load_data[:, 3])
        return self.max_capacity - power_assigned

    def calculate_reward(self, status, load, priority, load_data):
        # calculate dlf before returning reward
        load_data_temp = load_data.copy()
        load_data_temp[:, 3] = status

        power_values_from_dlf, _ = dlf_analyse(self.line_data, load_data_temp, grid_name=self.grid_name)

        power_values_from_dlf = np.array(power_values_from_dlf)

        if not (power_values_from_dlf.min() > 0.9 and power_values_from_dlf.max() < 1.1):
            return -np.sum(status)

        return np.sum(load * status * np.square(priority))

    def step(self, action):
        # Execute one time step within the environment
        print("ACTION: {}".format(action))

        if self.action_type == "continous":
            action = np.array(action)
            action[0] = 1

        obs = self.get_observation(action)
        reward = self.reward(action)
        print("REWARD {}".format(reward))

        load_data_copy = self.load_data.copy()
        load_data_copy[:, 3] = action
        power_values_from_dlf, _ = dlf_analyse(self.line_data, load_data_copy, grid_name=self.grid_name)

        power_values_from_dlf = np.array(power_values_from_dlf)
        restored_load = np.sum(load_data_copy[:, 1][(load_data_copy[:, 3] == 1)] / np.sum(load_data_copy[:, 1])) * 100
        self.done = True
        reward=reward if self.action_type == 'discrete' else reward[0]
        return obs, reward, self.done, {"min" : power_values_from_dlf.min(),"max" : power_values_from_dlf.max(), "load": restored_load}

    def reset(self):
        print("**** EPISODE STARTS ...\n")
        if self.action_type == "continous":
            # Reset the state of the environment to an initial state
            status = self.load_data[:, 3]
            self.load_data, self.line_data = get_data_from_csv(self.grid_name)

            self.load_data[:, 3] = status
        else:
            # Reset the state of the environment to an initial state
            status = self.load_data[:, 3]
            self.load_data, self.line_data = get_data_from_csv(self.grid_name)
            # print("Load data {}".format(self.load_data[:, 1]))
            self.load_data[:, 3] = status
        self.num_actions = 0

        self.done = False

        print("OBSERVATIONS: {}".format(self.current_state()))
        return self.current_state()

    def get_observation(self, action=np.inf):
        if self.action_type == "discrete":
            if action == np.inf:
                return self.current_state()
            else:
                if action <= self.n_nodes:
                    self.act_from_num(action=action)
                    print(action)
                else:
                    action_str = get_bin_str_with_max_count(action, self.n_nodes)
                    self.act(action_str)
                    print(action_str)
                # print("CURRENT STATE: " + str(self.load_data[:, 3]))

                return self.current_state()

        elif self.action_type == "continous":
            if not isinstance(action, np.ndarray):
                if action == np.inf:
                    return self.current_state()

            print("ACTION REWARD {}".format(
                self.calculate_reward(action, self.load_data[:, 1], self.load_data[:, 4], self.load_data)))
            print("OBSERVATION REWARD {}".format(self.current_reward))

            print("PRIORITY: " + str(self.load_data[:, 4]))

            if self.calculate_reward(np.array(action), self.load_data[:, 1], self.load_data[:, 4], self.load_data) > self.current_reward:
                self.load_data[:, 3] = np.array(action)
                return self.load_data[:, 3]
            else:
                return self.load_data[:, 3]

    def act_from_num(self, action):
        if action == 0:
            pass
        elif self.load_data[:, 3][action - 1] == 0:
            self.load_data[:, 3][action - 1] = 1
        else:
            self.load_data[:, 3][action - 1] = 0

        self.load_data[:, 3][0] = 1

    def act(self, action_str):
        for action in range(len(action_str)):
            print(action_str)
            self.load_data[:, 3][action] = int(action_str[action])

        self.load_data[:, 3][0] = 1
        return

    def current_state(self):
        return self.load_data[:, 3]

    def restored_load_percentage(self):
        load_data, line_data = get_data_from_csv(self.grid_name)
        return np.sum(load_data[:, 1][(self.load_data[:, 3] == 1)] / np.sum(load_data[:, 1])) * 100

    def reward(self, action):
        print("CURRENT STATE: " + str(self.load_data[:, 3]))
        print("RESTORED LOAD: {}%".format(self.restored_load_percentage()))
        power_values_from_dlf, _ = dlf_analyse(self.line_data, self.load_data, grid_name=self.grid_name)

        power_values_from_dlf = np.array(power_values_from_dlf)
        # print(power_values_from_dlf)
        print("MIN VOL: {}".format(power_values_from_dlf.min()))
        print("MAX VOL: {}".format(power_values_from_dlf.max()))

        if self.action_type == "continous":
            if self.calculate_reward(np.array(action), self.load_data[:, 1],
                                     self.load_data[:, 4], self.load_data) <= self.current_reward:
                return self.calculate_reward(np.array(action), self.load_data[:, 1],
                                             self.load_data[:, 4], self.load_data) - self.current_reward

        status_reward = self.calculate_reward(self.load_data[:, 3], self.load_data[:, 1], self.load_data[:,
                                                                                          4], self.load_data) # np.sum(self.load_data[:, 3] * np.square(self.load_data[:, 4]))

        # print("STATUS REWARD: {}".format(status_reward))

        self.current_reward = status_reward  # divide by num_actions which is the number of episodes
        return status_reward

    def power_assigned(self):
        return np.sum(self.load_data[:, 1] * self.load_data[:, 3])
