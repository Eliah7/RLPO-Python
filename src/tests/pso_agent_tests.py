# Authored by elia on 04/11/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
from unittest import TestCase
from src.main.agents.pso_agent import *
from src.main.env.environment import *

class PSOAgentTests(TestCase):

   def test_create_agent(self):
       env = Environment(3000)
       pso_agent = PSOAgent(env=env)
       print(pso_agent.predict(observation=3))
       pass