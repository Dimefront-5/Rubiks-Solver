'''
Created on Oct 23, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solveTopCross as solveTopCross
import rubik.validTopCross as validTopCross

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
#            outputDict['rotations']: string, directions to solve top Cross
#            outputDict['cube']: rotated cube to be returned for solving the top Face
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube that has a top cross
#        test 011: test 010, with another cube
#        test 020: nominal valid cube that has a straight line on top
#        test 021: test 020, with another cube
#        test 030: nominal valid cube that has a l on top
#        test 031: test 030, with another cube
#        test 040: nominal valid cube that has nothing on top
#        test 041: test 040, with another cube
#
#    no sad path
#
#
#Happy Path


    def test_solveTopCross_010_ShouldReturnSolvedTopCrossFromTopCross(self):
        cube = 'yryrrrrrrbgoggggggybyoooooooogbbbbbbbygyyyryrwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopCross_011_ShouldReturnSolvedTopCrossFromTopCross(self):
        cube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopCross_020_ShouldReturnSolvedTopCrossFromLine(self):
        cube = 'gbyggggggbyoooooooygobbbbbbbyrrrrrrryygoyryyrwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopCross_021_ShouldReturnSolvedTopCrossFromLineButNeedsToBeTurned(self):
        cube = 'yyoooooooybybbbbbboyyrrrrrrrorggggggggbyyybrgwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solveTopCross_030_ShouldReturnSolvedTopCrossFromL(self):
        cube = 'byygggggggyrooooooyrrbbbbbbggorrrrrryybyyoybowwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopCross_031_ShouldReturnSolvedTopCrossFromLButNeedsToTurn(self):
        cube = 'gyrooooooyrrbbbbbbggorrrrrrbyyggggggyyybyyoobwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopCross_040_ShouldReturnSolvedTopCrossFromNothing(self):
        cube = 'oyyoooooogybbbbbbbryyrrrrrrryyggggggggyrybboowwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solveTopCross_041_ShouldReturnSolvedTopCrossFromNothing(self):
        cube = 'oyyoooooogybbbbbbbryyrrrrrrryyggggggggyryobobwwwwwwwww'
        
        expectedResult = True
       
        
        actualResultCube = solveTopCross._solveTopCross(cube)
        
        actualResult = validTopCross._validTopCross(actualResultCube['cube'])
        
        self.assertEqual(expectedResult, actualResult)

#100 _lturn
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
#        test 010: cube with l in the right spot
#        test 020: cube with a l not in the right spot
#        test 030: cube with no l

    def test_lturn_110_ShouldReturnTheRotatedCubeFromL(self):
        cube = 'gybooooooyyobbbbbbybrrrrrrryrrggggggbygyygyoowwwwwwwww'
        
        expectedRotations = 'FURurf'
        
        actualResult = solveTopCross._lTurn(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_lturn_120_ShouldReturnTheRotatedCubeFromLInWrongSpot(self):
        cube = 'oyyobbbbbbybrrrrrrryrrgggggggyboooooyyboyyoggwwwwwwwww'
        
        expectedRotations = 'UUUFURurf'
        
        actualResult = solveTopCross._lTurn(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])

    def test_lturn_130_ShouldReturnTheSameCubeFromNoL(self):
        cube = 'gyyoooooobyybbbbbbryorrrrrrbyyggggggybggyoorrwwwwwwwww'
        
        expectedRotations = ''
        
        actualResult = solveTopCross._lTurn(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
#200 _lineturn
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
#        test 010: cube with line in the right spot
#        test 020: cube with a line not in the right spot
#        test 030: cube with no line

    def test_lineTurn_210_ShouldReturnRotatedCubeFromLine(self):
        cube = 'bryggggggryoooooooboybbbbbbgyyrrrrrroyygybrygwwwwwwwww'
        
        expectedRotations = 'FURurf'
        
        actualResult = solveTopCross._lineTurn(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_lineTurn_220_ShouldReturnRotatedCubeFromLineThatIsSideways(self):
        cube = 'ryoooooooboybbbbbbgyyrrrrrrbryggggggrgoyyygbywwwwwwwww'
        
        expectedRotations = 'UFURurf'
        
        actualResult = solveTopCross._lineTurn(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_lineTurn_230_ShouldReturnTheSameCubeFromNoLine(self):
        cube = 'gyyoooooobyybbbbbbryorrrrrrbyyggggggybggyoorrwwwwwwwww'
        
        expectedRotations = ''
        
        actualResult = solveTopCross._lineTurn(cube)
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
#Happy path
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()