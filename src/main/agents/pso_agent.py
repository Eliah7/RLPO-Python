# Authored by elia on 04/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from py4j.java_gateway import JavaGateway, GatewayParameters
from src.main.util.config import *
from src.main.env.environment import *

class PSOAgent:
    """
    Agent based on Particle Swarm Optimization

    """

    def __init__(self, env, num_iterations=100):
        self.gateway = JavaGateway(gateway_parameters=GatewayParameters(port=DEFAULT_PSO_AGENT_PORT))
        self.pso_app = self.gateway.entry_point
        self.env = env
        self.num_iterations = num_iterations

    def predict(self, observation):
        nodes = self.env.load_data[:, 0]
        power_values = self.env.load_data[:, 1]

        items = self.gateway.new_array(self.gateway.jvm.ac.udsm.dca.bpso.Item, len(nodes))

        values = self.gateway.new_array(self.gateway.jvm.double, len(nodes))

        for i in range(len(nodes)):
            values[i] = float(nodes[i])

        weights = self.gateway.new_array(self.gateway.jvm.double, len(power_values))

        for i in range(len(power_values)):
            weights[i] = float(power_values[i])

        for i in range(len(items)):
            item = self.gateway.jvm.ac.udsm.dca.bpso.Item(values[i], weights[i])
            items[i] = item

        problem = self.gateway.jvm.ac.udsm.dca.bpso.Problem(len(nodes), items, float(self.env.max_capacity))
        pso_for_problem = self.gateway.jvm.ac.udsm.dca.bpso.PSO(len(nodes), problem, self.num_iterations)
        result = pso_for_problem.solveForRL()

        result_str = ''
        for i in result:
            result_str += '{}'.format(i)

        return binary_str_to_int(result_str)


if __name__ == '__main__':
    agent = PSOAgent(env=Environment(15))






