from common.preprocessing import *
from common.rl import *
import torch.optim as optim
from torch.optim import Adam
import json

class DQN:
    def __init__(self, building_ids, 
                 buildings_states_actions, 
                 building_info,
                 observation_spaces = None,
                 action_spaces = None):     
        with open(buildings_states_actions) as json_file:
            self.buildings_states_actions = json.load(json_file)

        self.action_spaces = {uid: a_space for uid, a_space in zip(building_ids, action_spaces)}
        self.observation_spaces = {uid: o_space for uid, o_space in zip(building_ids, observation_spaces)}
            
    def select_action(self, states):        
        actions = np.array([
            0, 0, # building 1
            0, 0, # building 2
            0,    # building 3
            0,    # building 4
            0, 0, # building 5
            0, 0, # building 6
            0, 0, # building 7
            0, 0, # building 8
            0, 0, # building 9
        ])
        return actions, None
                
        
    def add_to_buffer(self, states, actions, rewards, next_states, done, coordination_vars=None, coordination_vars_next=None):
        
        '''Make any updates to your policy, you don't have to use all the variables above (you can leave the coordination
        variables empty if you wish, or use them to share information among your different agents). You can add a counter
        within this function to compute the time-step of the simulation, since it will be called once per time-step'''
        
        