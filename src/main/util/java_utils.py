# Authored by elia on 31/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here

"""

"""
from py4j.java_gateway import JavaGateway
# from src.main.env.environment import *
from src.main.util.model_utils import *

def dlf_analyse(line_data, load_data, grid_name="bus33"):
    gateway = JavaGateway()
    dlf_app = gateway.entry_point

    for i in range(len(load_data[:, 1])):
        if load_data[:, 3][i] == 0:
            load_data[:, 1][i] = 0

    line_data_n = get_java_line_data(line_data, gateway)
    load_data_n = get_java_load_data(load_data, gateway)

    mva, kva = get_mva_kva(grid_name=grid_name)

    dlf_app.setBusData(load_data_n)
    dlf_app.setLineData(line_data_n)
    dlf_app.setBaseMva(mva)
    dlf_app.setBaseKva(kva)
    dlf_app.setCentralBus(1)

    power_loss = dlf_app.calculate()

    power_values = []
    for value in dlf_app.getPowerValues():
        power_values.append(value)

    return power_values, power_loss

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

# if __name__ == '__main__':
#     env = Environment(3000)
#     print(dlf_analyse(env))

