# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from unittest import TestCase
from main.env.environment import Environment

class TestEnvironment(TestCase):
    def testCreateEnvironment(self):
        self.environment = Environment(3000)
        pass