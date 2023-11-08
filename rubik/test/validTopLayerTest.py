'''
Created on Nov 5, 2022

@author: Tyler Ray
'''
import unittest
import rubik.validTopLayer as validTopLayer

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
#            True: If the cube already has a top solved layer
#            False: If the cube doesn't have a top solved layer
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube that is already solved
#        test 011: another nominal valid cube that is already solved
#        test 020: nominal valid cube that has doesn't have the corners matching
#        test 030: nominal valid cube with one side completed and corners matching
#        test 040: nominal valid cube that has all corners matching
#
#    no sad path

    def test_validTopLayer_010_ShouldReturnTrueFromSolvedCube(self):
        cube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        actualResult = validTopLayer._validTopLayer(cube)
                
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopLayer_011_ShouldReturnTrueFromSolvedCube(self):
        cube = 'rrrrrrrrrooooooooobbbbbbbbbyyyyyyyyywwwwwwwwwggggggggg'
        
        expectedResult = True
       
        actualResult = validTopLayer._validTopLayer(cube)
                
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_validTopLayer_020_ShouldReturnTrueFromUnSolvedCube(self):
        cube = 'grbrrrrrrrggggggggoboooooooborbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = False
       
        actualResult = validTopLayer._validTopLayer(cube)
                
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopLayer_030_ShouldReturnFalseFromUnSolvedCubeWithMatchingCornersAndSolvedSide(self):
        cube = 'rbrrrrrrrobooooooobobbbbbbbyyyyyyyyywwwwwwwwwggggggggg'
        
        expectedResult = False
       
        actualResult = validTopLayer._validTopLayer(cube)
                
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopLayer_040_ShouldReturnTrueFromAllCornersMatching(self):
        cube = 'rbrrrrrrrobooooooobybbbbbbbyoyyyyyyywwwwwwwwwggggggggg'
        
        expectedResult = False
       
        actualResult = validTopLayer._validTopLayer(cube)
                
        self.assertEqual(expectedResult, actualResult)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()