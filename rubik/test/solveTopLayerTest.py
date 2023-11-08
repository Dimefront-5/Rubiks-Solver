'''
Created on Nov 5, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solveTopLayer as solveTopLayer
import rubik.validTopLayer as validTopLayer

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
#            outputDict['cube']: rotated cube to be returned that is solved
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube that is already solved
#        test 020: nominal valid cube that has one corner matching and the others aren't
#        test 030: nominal valid cube with one side completed and corners matching
#        test 040: nominal valid cube that has all corners matching
#        test 050: nominal valid cube that has one face complete and the others aren't matching
#        test 060: nominal valid cube that doesn't have any corners matching 
#    sad path:
#        test 010: abnormal cube with turned corner

    def test_solveTopLayer_010_ShouldReturnSolvedCubeFromSolvedCube(self):
        cube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = ''
       
        actualResult = solveTopLayer._solveTopLayer(cube)
                
        self.assertEqual(expectedRotations, actualResult.get('rotations'))
        
    def test_solveTopLayer_020_ShouldReturnSolvedCubeFromDifferentSolvedCube(self):
        cube = 'gggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwwwrrrrrrrrr'
        
        expectedRotations = ''
       
        actualResult = solveTopLayer._solveTopLayer(cube)
                
        self.assertEqual(expectedRotations, actualResult.get('rotations'))
        
    def test_solveTopLayer_020_ShouldReturnSolvedCubeFromOneMatchingCorners(self):
        cube = 'gbbrrrrrrrogggggggorooooooobgrbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        actualResult = solveTopLayer._solveTopLayer(cube)
        
        actualResult = validTopLayer._validTopLayer(actualResult['cube'])
    
                
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopLayer_030_ShouldReturnSolvedCubeFromNoMatchingCorners(self):
        cube = 'orrbbbbbbgobrrrrrrrgoggggggbbgooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        actualResult = solveTopLayer._solveTopLayer(cube)
    
        actualResult = validTopLayer._validTopLayer(actualResult['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solveTopLayer_040_ShouldReturnSolvedCubeFromAllMacthingCorners(self):
        cube = 'ogooooooobobbbbbbbrrrrrrrrrgbgggggggyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        actualResult = solveTopLayer._solveTopLayer(cube)
        
        actualResult = validTopLayer._validTopLayer(actualResult['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopLayer_050_ShouldReturnSolvedCubeFromMacthingCornersButTheSolvedFaceIsInTheRight(self):
        cube = 'ogooooooorrrrrrrrrbobbbbbbbgbgggggggyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        actualResult = solveTopLayer._solveTopLayer(cube)
        
        actualResult = validTopLayer._validTopLayer(actualResult['cube'])
        
        self.assertEqual(expectedResult, actualResult)  
        
#------- Sad Path

    def test_solveTopLayer_910_ShouldReturnErrorFromUnsolvableCube(self):
        cube = 'bbbbbbbbrbggrrrrrrorrgggggggooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = 'error: unsolvable cube'
       
        actualResult = solveTopLayer._solveTopLayer(cube)
                
        self.assertEqual(expectedResult, actualResult['status'])  
        
        
        
        
#100 _allMatchingCorners
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        outputDict:
#                cube: rotated cube
#                rotations: the rotations it took to get to the rotated cube
#    Happy path analysis
#        test 010: cube with No finished Face
#        test 020: Cube with finished Face on Front to turn Clockwise
#        test 030: Cube with finished Face on Right To turn Clockwise
#        test 040: Cube with finished Face on Back to turn Clockwise
#        test 050: Cube with finished Face on Left to turn Clockwise
#        test 060: Cube with finished Face on Front to turn Counter-Clockwise
#        test 070: Cube with finished Face on Right To turn Counter-Clockwise
#        test 080: Cube with finished Face on Back to turn Counter-Clockwise
#        test 090: Cube with finished Face on Left to turn Counter-Clockwise
#        test 100: Cube that has a finished Face but needs the top to be turned to find it
#Happy path

    def test_allMatchingCorners_010_cubeWithSolvedFaceOnFrontNeedToTurnClockwise(self):
        cube = 'bbbbbbbbbrorrrrrrrgrgggggggogoooooooyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'BBURlBBrLUBB'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
        
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_allMatchingCorners_020_cubeWithSolvedFaceOnRightNeedToTurnClockwise(self):
        cube = 'ogooooooobbbbbbbbbrorrrrrrrgrgggggggyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'LLUfBLLFbULL'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)        
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_allMatchingCorners_030_cubeWithSolvedFaceOnBackNeedToTurnClockwise(self):
        cube = 'grgggggggogooooooobbbbbbbbbrorrrrrrryyyyyyyyywwwwwwwww'
        
        expectedRotations = 'FFUrLFFRlUFF'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)        
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_allMatchingCorners_040_cubeWithSolvedFaceOnLeftNeedToTurnClockwise(self):
        cube = 'rorrrrrrrgrgggggggogooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'RRUFbRRfBURR'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_allMatchingCorners_050_cubeWithSolvedFaceOnFrontNeedsToTurnCounter(self):
        cube = 'bbbbbbbbbrgrrrrrrrgogggggggoroooooooyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'BBuRlBBrLuBB'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_allMatchingCorners_060_cubeWithSolvedFaceOnRightNeedsToTurnCounter(self):
        cube = 'orooooooobbbbbbbbbrgrrrrrrrgogggggggyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'LLufBLLFbuLL'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_allMatchingCorners_070_cubeWithSolvedFaceOnBackNeedsToTurnCounter(self):
        cube = 'gogggggggorooooooobbbbbbbbbrgrrrrrrryyyyyyyyywwwwwwwww'
        
        expectedRotations = 'FFurLFFRluFF'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_allMatchingCorners_080_cubeWithSolvedFaceOnLeftNeedsToTurnCounter(self):
        cube = 'rgrrrrrrrgogggggggorooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'RRuFbRRfBuRR'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_allMatchingCorners_090_cubeWithNoSolvedFaceThatNeedsToTurnCounter(self):
        cube = 'rgrrrrrrrgogggggggobooooooobrbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'BBuRlBBrLuBB'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
        
        actualSolvedCube = validTopLayer._validTopLayer(actualResult['cube'])
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        self.assertEqual(False, actualSolvedCube)
        
        
    def test_allMatchingCorners_1100_cubeThatNeedsToBeTurnedToBeSolved(self):
        cube = 'bbbrrrrrrrgrgggggggogooooooorobbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'URRuFbRRfBuRR'
       
        actualResult = solveTopLayer._allMatchingCorners(cube)
        
        actualSolvedCube = validTopLayer._validTopLayer(actualResult['cube'])
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        self.assertEqual(True, actualSolvedCube)


#200 _oneMatchingCorner
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        outputDict:
#                cube: rotated cube
#                rotations: the rotations it took to get to the rotated cube
#    Happy path analysis
#        test 010: cube that has matching corners on the front
#        test 020: cube that has matching corners on the right
#        test 030: cube that has matching corners on the back
#        test 040: cube that has matching corners on the left
#Happy path

    def test_oneMatchingCorner_210_matchingCornersOnTheFront(self):
        cube = 'orooooooobbrbbbbbbgobrrrrrrrggggggggyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'fUBuFUUbUBUUb'
       
        actualResult = solveTopLayer._oneMatchingCorner(cube)
                        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_oneMatchingCorner_220_matchingCornersOnTheRight(self):
        cube = 'rggggggggorooooooobbrbbbbbbgobrrrrrryyyyyyyyywwwwwwwww'
        
        expectedRotations = 'rULuRUUlULUUl'
       
        actualResult = solveTopLayer._oneMatchingCorner(cube)
                        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_oneMatchingCorner_230_matchingCornersOnTheBack(self):
        cube = 'gobrrrrrrrggggggggorooooooobbrbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'bUFuBUUfUFUUf'
       
        actualResult = solveTopLayer._oneMatchingCorner(cube)
                        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_oneMatchingCorner_240_matchingCornersOnTheLeft(self):
        cube = 'bbrbbbbbbgobrrrrrrrggggggggoroooooooyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'lURuLUUrURUUr'
       
        actualResult = solveTopLayer._oneMatchingCorner(cube)
                        
        self.assertEqual(expectedRotations, actualResult['rotations'])



#300 _checkingForMatchingCorners
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        outputDict:
#                cube: rotated cube
#                rotations: the rotations it took to get to the rotated cube
#    Happy path analysis
#        test 010: cube that has no matching corners
#        test 020: cube that has 1 matching corner
#        test 030: cube that has 4 matching corners (I have never seen a cube with 2 or 3)
#Happy path


    def test_checkingForMatchingCorners_310_NoMatchingCorners(self):
        cube = 'obrbbbbbbgobrrrrrrrroggggggbggooooooyyyyyyyyywwwwwwwww'
        
        expectedRotations = 'lURuLUUrURUUr'
       
        actualResult = solveTopLayer._checkingForMatchingCorners(cube)
                        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_checkingForMatchingCorners_320_oneMatchingCorner(self):
        cube = 'bggoooooooobbbbbbbrbrrrrrrrgroggggggyyyyyyyyywwwwwwwww'
        
        expectedCount = 1
       
        actualResult = solveTopLayer._checkingForMatchingCorners(cube)
                        
        self.assertEqual(expectedCount, actualResult['count'])
        
    def test_checkingForMatchingCorners_330_allMatchingCorners(self):
        cube = 'bobbbbbbbrbrrrrrrrgggggggggorooooooooyyyyyyyyywwwwwwwww'
        
        expectedCount = 4
       
        actualResult = solveTopLayer._checkingForMatchingCorners(cube)
                        
        self.assertEqual(expectedCount, actualResult['count'])
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()