'''
Created on Nov 9, 2022

@author: Tyler Ray
'''
import unittest
import rubik.validSolvedCube as validSolvedCube
# Analysis
#
#    inputs:
#        cube: string, mandatory, validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: boolean
#        nominal:
#            True: If the cube is already solved
#            False: If the cube isn't solved
#
#    confidence level: boundary value analysis
#
#    happy path:
#        test 010: A valid solved cube
#        test 011: a valid solved cube again
#        test 020: a valid solved cube with a color other than white on bottom
#        test 030: a valid unsolved cube


class Test(unittest.TestCase):


    def test_validSolvedCube_010_validSolvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = True
        
        actualResult = validSolvedCube._validSolvedCube(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validSolvedCube_011_validSolvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        
        expectedResult = True
        
        actualResult = validSolvedCube._validSolvedCube(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validSolvedCube_020_validSolvedCube(self):
        cube = 'ooooooooogggggggggyyyyyyyyywwwwwwwwwbbbbbbbbbrrrrrrrrr'
        
        expectedResult = True
        
        actualResult = validSolvedCube._validSolvedCube(cube)
        
        self.assertEqual(expectedResult, actualResult)

    def test_validSolvedCube_030_validUnsolvedCube(self):
        cube = 'gbbbbbbbbrrrrrrrrrbggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = False
        
        actualResult = validSolvedCube._validSolvedCube(cube)
        
        self.assertEqual(expectedResult, actualResult)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()