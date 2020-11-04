# Authored by elia on 04/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from py4j.java_gateway import JavaGateway, GatewayParameters
from src.main.util.config import *

class PSOAgent:
    """
    Agent based on Particle Swarm Optimization

    """

    def __init__(self, env):
        self.gateway = JavaGateway(gateway_parameters=GatewayParameters(port=DEFAULT_PSO_AGENT_PORT))
        self.pso_app = self.gateway.entry_point
        self.env = env

        # print(self.gateway.jvm.ac.udsm.dca.bpso.Item)
        # print(self.gateway.jvm.ac.udsm.dca.bpso.Problem)
        # print(self.pso_app.printInt())

    def predict(self, observation):
        items = self.gateway.new_array(self.gateway.jvm.ac.udsm.dca.bpso.Item, 33)

        java_values = [0.0, 500.0, 450.0, 1200.0, 300.0, 60.0, 1000.0, 200.0, 60.0, 60.0, 225.0, 600.0, 60.0, 600.0, 60.0, 60.0, 60.0, 450.0, 450.0, 900.0, 900.0,
                     450.0, 90.0, 2100.0, 60.0, 60.0, 300.0, 1200.0, 200.0, 750.0, 210.0, 300.0, 300.0]

        values = self.gateway.new_array(self.gateway.jvm.double, len(java_values))

        for i in range(len(java_values)):
            values[i] = float(java_values[i])

        max_capacity = 15.0

        java_weights = [0.0, 500.0, 450.0, 1200.0, 300.0, 60.0, 1000.0, 200.0, 60.0, 60.0, 225.0, 600.0, 60.0, 600.0,
                       60.0, 60.0, 60.0, 450.0, 450.0, 900.0, 900.0,
                       450.0, 90.0, 2100.0, 60.0, 60.0, 300.0, 1200.0, 200.0, 750.0, 210.0, 300.0, 300.0]

        weights = self.gateway.new_array(self.gateway.jvm.double, len(java_weights))

        for i in range(len(java_weights)):
            weights[i] = float(java_weights[i])

        for i in range(len(items)):
            item = self.gateway.jvm.ac.udsm.dca.bpso.Item(values[i], weights[i])
            items[i] = item

        problem = self.gateway.jvm.ac.udsm.dca.bpso.Problem(33, items, max_capacity)
        pso_for_problem = self.gateway.jvm.ac.udsm.dca.bpso.PSO(33, problem, 100)
        result = pso_for_problem.solveForRL()

        result_str = ''
        for i in result:
            result_str += '{} '.format(i)

        print(result_str)






