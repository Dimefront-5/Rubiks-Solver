'''
Created on Aug 29, 2022

@author: Tyler Ray
'''
import unittest
import rubik.cube as cube

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

# Analysis:    Cube: class
#    methods:    instantiate
#                 rotate
#                 toString
#
# Analysis:    cube.___init__
#    inputs:
#        initialCube: string; string; len=54, [brgoyw], 9 occurrences of each character, unique middle color; mandatory; arrives unvalidated
#    output:
#        side effects: none
#        nominal:
#            Instance of Cube
#        abnormal:
#            exception

    def test_init_010_ShouldInstantiateCube(self):
        incomingCube = 'orrwobowoygrobogrbbyggryoorrobbgryrgwgwwywwybwbybwggyy'
        myCube = cube.Cube(incomingCube)
        self.assertIsInstance(myCube, cube.Cube)
