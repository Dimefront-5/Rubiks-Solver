'''
Created on Oct 23, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solveTopFace as solveTopFace
import rubik.validTopFace as validTopFace

class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#        cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: dict
#        nominal:
#            outputDict['rotations']: string, directions to solve top Face
#            outputDict['cube']: rotated cube to be returned for next solve piece
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube that is already solved
#        test 020: nominal valid cube that has a top Face
#        test 030: nominal valid cube that starts with a fish
#        test 031: test 030, but the fish needs to be turned
#        test 040: nominal valid cube that has a straight line on top
#        test 050: nominal valid cube that has a l on top
#        test 051: test 050, but with a different cube
#        test 060: nominal valid cube that has nothing on top
#        test 061: test 060, but with a different cube
#        test 070: nominal valid cube that isn't yellow on top
#
#    sad path:
#        test 910: abnormal cube that is unsolvable

    def test_solveTopFace_010_ShouldReturnSolvedCube(self):
        cube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = ''
       
        
        actualResult = solveTopFace._solveTopFace(cube)
        
        self.assertEqual(expectedRotations, actualResult.get('rotations'))
        
        
    def test_solveTopFace_020_ShouldReturnSolvedCubeFromTopFace(self):
        cube = 'yryrrrrrrbgoggggggybyoooooooogbbbbbbbygyyyryrwwwwwwwww'
        
        expectedResult = True
       
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        isTopValid = validTopFace._validTopFace(actualResultCube['cube'])
        
        
        self.assertEqual(expectedResult, isTopValid)
        
        
    def test_solveTopFace_030_ShouldReturnSolvedCubeFromTopFaceWithFishInStartingPosition(self):
        cube = 'royoooooogbybbbbbboryrrrrrrrgbgggggggybyyyyyowwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        isTopValid = validTopFace._validTopFace(actualResultCube['cube'])
        
        
        self.assertEqual(expectedResult, isTopValid)
        
    def test_solveTopFace_031_ShouldReturnSolvedCubeFromTopFaceWithFishNotInStartingPosition(self):
        cube = 'gbyooooooorybbbbbbrgbrrrrrrroyggggggyygyyyoybwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        isTopValid = validTopFace._validTopFace(actualResultCube['cube'])
        
        
        self.assertEqual(expectedResult, isTopValid)
        
        
    def test_solveTopFace_040_ShouldReturnSolvedTopFaceFromLineButNeedsToBeTurned(self):
        cube = 'yyoooooooybybbbbbboyyrrrrrrrorggggggggbyyybrgwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        actualResult = validTopFace._validTopFace(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult) 
        
        
    def test_solveTopFace_050_ShouldReturnSolvedTopFaceFromLButNeedsToTurn(self):
        cube = 'gyrooooooyrrbbbbbbggorrrrrrbyyggggggyyybyyoobwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        actualResult = validTopFace._validTopFace(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solveTopFace_051_ShouldReturnSolvedTopFaceFromL(self):
        cube = 'byygggggggyrooooooyrrbbbbbbggorrrrrryybyyoybowwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        actualResult = validTopFace._validTopFace(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    
    def test_solveTopFace_060_ShouldReturnSolvedCubeFromNoFace(self):
        cube = 'rryrrrrrrryoggggggbgoooooooyybbbbbbbgyybyoyygwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        isTopValid = validTopFace._validTopFace(actualResultCube['cube'])
        
        
        self.assertEqual(expectedResult, isTopValid)   
        
        
        
    def test_solveTopFace_061_ShouldReturnSolvedTopFaceFromNothing(self):
        cube = 'ryoggggggbyoooooooyybbbbbbbryyrrrrrryggbyrgoywwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        actualResult = validTopFace._validTopFace(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solveTopFace_070_ShouldReturnSolvedTopFaceFromNotYellowOnTop(self):
        cube = 'ooyyyyyyyoowggggggbbwwwwwwwoggbbbbbbgoooowyybrrrrrrrrr'
        
        expectedResult = True
       
        
        actualResultCube = solveTopFace._solveTopFace(cube)
        
        actualResult = validTopFace._validTopFace(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
        
# ---- Sad Path
    def test_solveTopFace_910_ShouldReturnErrorFromUnsolvableCube(self):
        cube = 'oorggggggygyoooooorbybbbbbborgrrrrrrbygyyyyybwwwwwwwww'
        
        expectedResult = 'error: unsolvable cube'
       
        actualResult= solveTopFace._solveTopFace(cube)
                
        self.assertEqual(expectedResult, actualResult['status'])
        
#100 _findingFish
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        returnDict:
#                cube: rotated cube
#                rotations: the rotations it took to get to the rotated cube
#
#    Happy path analysis
#        test 010: cube with no fish
#        test 020: cube with a fish in the right spot
#        test 030: cube with a fish not in the right spot
#Happy path

    def test_findingFish_110_ShouldReturnRotatedCubeFromFish(self):
        cube = 'ryoggggggbyoooooooyybbbbbbbryyrrrrrryggbyrgoywwwwwwwww'
        
        expectedResult = None
       
        actualResult = solveTopFace._findingFish(cube)
            
        self.assertEqual(expectedResult, actualResult)
        
    def test_findingFish_120_ShouldReturnRotatedCubeFromFish(self):
        cube = 'royoooooogbybbbbbboryrrrrrrrgbgggggggybyyyyyowwwwwwwww'
        
        expectedRotations = 'RUrURUUr'
       
        actualResult = solveTopFace._findingFish(cube)
            
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_findingFish_130_ShouldReturnRotatedCubeFromFishButNotInRightSpot(self):
        cube = 'gbyooooooorybbbbbbrgbrrrrrrroyggggggyygyyyoybwwwwwwwww'
        
        expectedRotations = 'UUURUrURUUr'
       
        actualResult = solveTopFace._findingFish(cube)
            
        self.assertEqual(expectedRotations, actualResult['rotations'])
        

#200 _positionCheck
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        returnDict:
#                cube: rotated cube
#                rotations: the rotations it took to get to the rotated cube
#
#    Happy path analysis
#        test 010: cube with yellow in the correct spot
#        test 020: cube that needs to be rotated to the right spot for yellow
#Happy path       

    def test_positionCheck_210_ShouldReturnRotatedCubeWhenYellowIsInRightSpot(self):
        cube = 'grorrrrrrbgrgggggggbrooooooyoybbbbbbbyyyyyoyywwwwwwwww'
        
        expectedRotations = 'RUrURUUr'
       
        actualResult = solveTopFace._positionCheck(cube)
            
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_positionCheck_220_ShouldReturnRotatedCubeWhenYellowIsntInRightSpot(self):
        cube = 'bgrgggggggbrooooooyoybbbbbbgrorrrrrroybyyyyyywwwwwwwww'
        
        expectedRotations = 'UUURUrURUUr'
       
        actualResult = solveTopFace._positionCheck(cube)
            
        self.assertEqual(expectedRotations, actualResult['rotations'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()