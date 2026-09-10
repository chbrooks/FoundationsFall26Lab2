from unittest import TestCase
from mars_planner import *


class Test(TestCase):

    def test_move_to_sample(self):
        s = RoverState(rover_loc="battery")
        s2 = move_to_sample(s)
        self.assertEqual(s2.rover_loc, "sample")

    def test_eq(self):
        s = RoverState(rover_loc="battery")
        s2 = RoverState(rover_loc="battery")
        self.assertEqual(s, s2)
        s3 = RoverState(rover_loc="station")
        self.assertNotEqual(s, s3)

    def test_successors(self):
        s = RoverState()
        slist = s.successors(action_list)
        print(slist)

    def test_move_to_station(self):
        s = RoverState(rover_loc="battery")
        s2 = move_to_station(s)
        self.assertEqual(s2.rover_loc, "station")
