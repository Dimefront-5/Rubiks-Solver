'''
Created on Oct 23, 2022

@author: Tyler Ray
'''
import unittest
import rubik.validTopFace as validTopFace


class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#        cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: boolean
#        True: if cube's top layer is solved
#        False: if cube's top layer isn't solved
#
#    confidence level: boundary value analysis
#
#    happy path:
#       
#        test 010: nominal valid cube that has the top layer solved
#        test 011: test 010, with another cube
#        test 020: nominal valid cube that doesn't have the top layer solved
#        test 021: test 020, with another cube
#        test 030: nominal valid cube that has part of the top layer solved
#        test 031: test 030, with another cube
#

    def test_validTopFace_010_ShouldReturnTrueFromSolvedCube(self):
        cube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        
        actualResult = validTopFace._validTopFace(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopFace_011_ShouldReturnTrueFromTopFaceSolvedCube(self):
        cube = 'ggorrrrrrbbgggggggooboooooorrrbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        
        actualResult = validTopFace._validTopFace(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopFace_020_ShouldReturnFalseFromSolvedCube(self):
        cube = 'ggorrrrrrbbgggggggoobooooooyrrbbbbbbryyyyyyyywwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopFace._validTopFace(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_validTopFace_021_ShouldReturnFalseFromSolvedCube(self):
        cube = 'ggorrrrrrbygggggggoobooooooyrrbbbbbbrybyyyyyywwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopFace._validTopFace(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopFace_030_ShouldReturnFalseFromPartlySolvedCube(self):
        cube = 'rbgrrrrrroybggggggyoyoooooorybbbbbbbgyogyryyywwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopFace._validTopFace(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_validTopFace_031_ShouldReturnFalseFromPartlySolvedCube(self):
        cube = 'rybrrrrrrygoggggggyoyoooooobyybbbbbbrygbyygrowwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopFace._validTopFace(cube)
        
        self.assertEqual(expectedResult, actualResult)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()