# Authored by elia on 31/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here

"""

"""
from py4j.java_gateway import JavaGateway
from src.main.env.environment import *

def dlf_analyse(env):
    gateway = JavaGateway()
    dlf_app = gateway.entry_point

    # env.load_data[:, 1] = [0 if status== 0 else for status in env.load_data[:, 4]]
    # for i in range(len(env.load_data[:, 1])):
    #     if env.load_data[:, 4][i] == 0:
    #         env.load_data[:, 1][i] = 0

    line_data = get_java_line_data(env.line_data, gateway)
    load_data = get_java_load_data(env.load_data, gateway)

    dlf_app.setBusData(load_data)
    dlf_app.setLineData(line_data)
    dlf_app.setCentralBus(1)

    return dlf_app.calculate()

def get_java_line_data(line_data, gateway):
    column_len = len(line_data)
    row_len = len(line_data[0])

    java_line_data = gateway.new_array(gateway.jvm.double, column_len, row_len)

    for i in range(column_len):
        for j in range(row_len):
            java_line_data[i][j] = line_data[i][j]

    return java_line_data

def get_java_load_data(load_data, gateway):
    column_len = len(load_data)
    row_len = len(load_data[0])

    java_load_data = gateway.new_array(gateway.jvm.double, column_len, row_len)

    for i in range(column_len):
        for j in range(row_len):
            java_load_data[i][j] = load_data[i][j]

    return java_load_data

if __name__ == '__main__':
    env = Environment(3000)
    print(dlf_analyse(env))

