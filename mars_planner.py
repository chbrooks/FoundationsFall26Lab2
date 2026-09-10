## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search, depth_first_search


class RoverState :
    def __init__(self, rover_loc="station",
                     sample_loc="site",
                     holding_sample=False, charged=False, prev=None):
        self.rover_loc = rover_loc
        self.sample_loc=sample_loc
        self.holding_sample = holding_sample
        self.charged=charged
        self.prev = prev

    ## you do this.
    def __eq__(self, other):
       pass


    def __repr__(self):
        return (f"Rover Location: {self.rover_loc}\n" +
                f"Sample Location?: {self.sample_loc}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.rover_loc = "sample"
    if r2.holding_sample :
        r2.sample_loc = "sample"
    r2.prev=state
    return r2
def move_to_station(state) :
    r2 = deepcopy(state)
    r2.rover_loc = "station"
    if r2.holding_sample :
        r2.sample_loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.rover_loc = "battery"
    if r2.holding_sample :
        r2.sample_loc = "station"
    r2.prev = state
    return r2
# add tool functions here


def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.rover_loc == state.sample_loc:
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.rover_loc == state.sample_loc:
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.rover_loc == "charger":
        r2.charged = True
    r2.prev = state
    return r2


action_list = [charge, drop_sample, pick_up_sample,
               move_to_sample, move_to_battery, move_to_station]


### sample goal functions.

def battery_goal(state) :
    return state.loc == "battery"


## add your goals here.



def mission_complete(state) :
    pass


if __name__=="__main__" :
    s = RoverState()
    result = breadth_first_search(s, action_list, mission_complete)
    print(result)



