'''
Created on Oct 10, 2022

@author: Tyler Ray
'''
import unittest
import rubik.validMiddleLayer as validMiddleLayer

class Test(unittest.TestCase):
    
# Analysis
#
#    inputs:
#        cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: boolean
#        nominal:
#            boolean: True if the middle layer is solved on the cube, false if not
#
#    confidence level: boundary value analysis
#
#    happy path:
#        test 010: cube with already solved middle layer
#        test 020: cube with middle layer solved for one side
#        test 030: cube with middle layer solved for two sides
#        test 040: cube with middle layer not solved at all
#        test 050: An already solved cube

# ----- Happy Path

    def test_solveMiddleLayer_010_cubeWithAlreadySolvedLayer(self):
        cube = 'ybyrrrrrrgygggggggyyyoooooobgbbbbbbbroryyroyowwwwwwwww'
        
        expectedResult = True
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solveMiddleLayer_011_CubeWithAlreadySolvedLayer(self):
        cube = 'yyyoooooobgbbbbbbbybyrrrrrrgygggggggoyoryyrorwwwwwwwww'
        
        expectedResult = True
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_020_CubeWithOneSolvedLayer(self):
        cube = 'bbygggggggbyooyoooryoobgbbbbryyrrrrryrgbyoryowwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_021_CubeWithOneSolvedLayer(self):
        cube = 'bryyrrrrrbbygggggggbyooyoooryoobgbbbgooryyybrwwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_022_CubeWithOneSolvedLayer(self):
        cube = 'ryoobgbbbbryyrrrrrbbygggggggbyooyooooyroybgrywwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_023_CubeWithOneSolvedLayer(self):
        cube = 'gbyooyoooryoobgbbbbryyrrrrrbbyggggggrbyyyroogwwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_030_CubeWithTwoSolvedLayer(self):
        cube = 'yyorrrrrrbbbggggggrgyooyoooryoobbbbbgyybyogrywwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_031_CubeWithTwoSolvedLayer(self):
        cube = 'ryoobbbbbyyorrrrrrbbbggggggrgyooyooogyybyogrywwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_032_CubeWithTwoSolvedLayer(self):
        cube = 'rgyooyoooryoobbbbbyyorrrrrrbbbgggggggyybyogrywwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_033_CubeWithTwoSolvedLayer(self):
        cube = 'bbbgggggggrgyooyoooryoobbbbbyyorrrrrryybyogrywwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_040_CubeWithNothing(self):
        cube = 'rggooyoooygyobbbbboygrrorrroybggbgggybbryyyrrwwwwwwwww'
        
        expectedResult = False
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveMiddleLayer_050_alreadySolvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = True
        
        actualResult = validMiddleLayer._validMiddleLayer(cube)
        
        self.assertEqual(expectedResult, actualResult)
        