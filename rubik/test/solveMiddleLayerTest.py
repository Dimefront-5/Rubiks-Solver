'''
Created on Oct 10, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solveMiddleLayer as solveMiddleLayer
import rubik.validMiddleLayer as validMiddleLayer

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
#            dict['rotations']: string, the amount of directions to solve middle layer
#            dict['cube']: string, the cube that has been solved for middle layer
#
#    confidence level: boundary value analysis
#
#    happy path:
#        test 010: cube with already solved middle layer
#        test 020: cube with middle layer solved for one side
#        test 030: cube with middle layer solved for two sides
#        test 040: cube with middle layer not solved at all
#        test 050: An already solved cube
#        test 060: Cube only needs one turn to finish
#    No sad path:
#        I do not think it is dynamically possible to catch an unsolvable cube at this layer. However I have a circuit breaker for the unforseen
# ----- Happy Path

    def test_solveMiddleLayer_010_cubeWithAlreadySolvedLayer(self):
        cube = 'ybyrrrrrrgygggggggyyyoooooobgbbbbbbbroryyroyowwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = ''
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
    
    def test_solveMiddleLayer_020_OneSideSolvedCube(self):
        cube = 'gobooooooryrbbybbbgbbgrgrrryryrgggggoyybyroyywwwwwwwww'
        
        expectedResult = True
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        actualResult2 = validMiddleLayer._validMiddleLayer(actualResult['cube'])
        expectedRotations = 'UuruRUBUbLUlubuBUUULUlubuB'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        self.assertEqual(expectedResult, actualResult2)  
        
    def test_solveMiddleLayer_030_TwoSidesSolvedCube(self):
        cube = 'bybooooooyrybbbbbbgygrryrrryyyogggggrbogygrrowwwwwwwww'
        
        expectedResult = True
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        actualResult2 = validMiddleLayer._validMiddleLayer(actualResult['cube'])
        expectedRotations = 'UUUULUlubuB'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        self.assertEqual(expectedResult, actualResult2)  
        
    def test_solveMiddleLayer_040_cubeWithNoMiddleLayerReady(self):
        cube = 'ygryoboooygoybobbbyrryrorrrgbbbgrgggyggryooybwwwwwwwww'
        
        expectedResult = True
        
        expectedRotations = 'UUUFUfuluLUUBUburuRUUUULUlubuBUUUufuFURUr'
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        actualResult2 = validMiddleLayer._validMiddleLayer(actualResult['cube'])
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        self.assertEqual(expectedResult, actualResult2)
        
    def test_solveMiddleLayer_041_cubeWithNoMiddleLayerReady(self):
        cube = 'gryyogooobobybrbbbyogbrorrrorrggbgggyyoyybygrwwwwwwwww'
        
        expectedResult = True
        
        expectedRotations = 'UUULUlubuBUUFUfuluLUUURUrufuFBUburuRUUUBUburuR'
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        actualResult2 = validMiddleLayer._validMiddleLayer(actualResult['cube'])
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        self.assertEqual(expectedResult, actualResult2) 
        
    def test_solveMiddleLayer_050_anAlreadySolvedCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = True
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        actualResult2 = validMiddleLayer._validMiddleLayer(actualResult['cube'])
        expectedRotations = ''
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        self.assertEqual(expectedResult, actualResult2) 
        
    def test_solveMiddleLayer_060_cubeWithMiddleLayerSolvedForOneSideWithOnlyOneTurn(self):
        cube = 'rgyggggggbybooooooyoobbbbbbyyyrryrrrgyobyrgrrwwwwwwwww'
        
        expectedResult = True
        
        actualResult = solveMiddleLayer._solveMiddleLayer(cube)
        actualResult = validMiddleLayer._validMiddleLayer(actualResult['cube'])
        
        self.assertEqual(expectedResult, actualResult)
 
#100 _findTopMiddleWithNoTopColors
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        outputDict:
#                cube: rotated cube
#                dir: the rotations it took to get to the rotated cube
#    Happy path analysis
#        test 010: cube with top middle colors on every top side cube
#        test 020: cube with first not being top middle
#        test 030: cube with second not being top middle
#        test 040: cube with third not being top middle
#        test 050: cube with fourth not being top middle
#Happy path

    def test_findTopMiddleWithNoTopColors_110_cubewithYellowsOnEveryTopSideCube(self):
        cube = 'rybgoboooyogobrbbborbgrbrrrryyrgogggyyygyygbowwwwwwwww'
        
        expectedResult = None
        
        actualResult = solveMiddleLayer._findTopMiddleWithNoTopColors(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_findTopMiddleWithNoTopColors_120_cubewithYellowsOnEveryTopSideCube(self):
        cube = 'oobyoboooryyobrbbbgyygrbrrrrryrgbgggggoyyobgywwwwwwwww'
        
        expectedRotations = 'uluLUFUf'
        
        actualResult = solveMiddleLayer._findTopMiddleWithNoTopColors(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_findTopMiddleWithNoTopColors__130_cubewithYellowsOnEveryTopSideCube(self):
        cube = 'rryrgbgggoobyoboooryyobrbbbgyygrbrrrooygyggybwwwwwwwww'
        
        expectedRotations = 'ufuFURUr'
        
        actualResult = solveMiddleLayer._findTopMiddleWithNoTopColors(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_findTopMiddleWithNoTopColors__140_cubewithYellowsOnEveryTopSideCube(self):
        cube = 'gyygrbrrrrryrgbgggoobyoboooryyobrbbbygboyyoggwwwwwwwww'
        
        expectedRotations = 'uruRUBUb'
        
        actualResult = solveMiddleLayer._findTopMiddleWithNoTopColors(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_findTopMiddleWithNoTopColors__150_cubewithYellowsOnEveryTopSideCube(self):
        cube = 'ryyobrbbbgyygrbrrrrryrgbgggoobyobooobyggygyoowwwwwwwww'
        
        expectedRotations = 'ubuBULUl'
        
        actualResult = solveMiddleLayer._findTopMiddleWithNoTopColors(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
#200 _findMiddleSidePieces
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        outputDict:
#                cube: rotated cube
#                dir: the rotations it took to get to the rotated cube
#    Happy path analysis
#        test 010: cube with first side being incorrect
#        test 020: cube with second side being incorrect
#        test 030: cube with second not being top middle
#        test 040: cube with third not being top middle
#        test 050: cube with fourth not being top middle
#Happy path

    def test_findMiddleSidePieces__210_cubeWithFirstIncorrectSide(self):
        cube = 'oyrobrbbbybygrbrrrroorgggggyryoobooogygyyybgbwwwwwwwww'
        
        expectedRotations = 'luLUFUf'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_findMiddleSidePieces__220_cubeWithSecondSideIncorrect(self):
        cube = 'byrbbybbbgggorbrrroobrgggggygyooyoooobyryyrrywwwwwwwww'
        
        expectedRotations = 'RUrufuF'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_findMiddleSidePieces__230_cubeWithThirdIncorrectSide(self):
        cube = 'rybbbbbbbyyyorbrrrrrgrgggggorbooyoooyggyyoygowwwwwwwww'
        
        expectedRotations = 'fuFURUr'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
    
    def test_findMiddleSidePieces__240_cubeWithFourthIncorrectSide(self):
        cube = 'yybbbbbbbrryrryrrrrrgggggggobbooyoooyygoygooywwwwwwwww'
        
        expectedRotations = 'BUburuR'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])  
        
    def test_findMiddleSidePieces__250_cubeWithFifthIncorrectSide(self):
        cube = 'grobbbbbbyyrrrrrrryobygggggygrooyoooobbyyoyggwwwwwwwww'
        
        expectedRotations = 'ruRUBUb'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations']) 
        
    def test_findMiddleSidePieces__260_cubeWithThirdIncorrectSide(self):
        cube = 'yorbbbbbbggyrrrrrroobggygggryoroyoooygboyygbywwwwwwwww'
        
        expectedRotations = 'LUlubuB'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_findMiddleSidePieces__270_cubeWithSeventhIncorrectSide(self):
        cube = 'yrybbbbbbrgrrrrrrryoyggggggoyoyoyooobbboyogygwwwwwwwww'
        
        expectedRotations = 'buBULUl'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_findMiddleSidePieces__280_cubeWithThirdIncorrectSide(self):
        cube = 'orgbbbbbbogyrrrrrrroyggggggbyyooyooorbgoyybyywwwwwwwww'
        
        expectedRotations = 'FUfuluL'
        
        actualResult = solveMiddleLayer._findMiddleSidePieces(cube)
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()