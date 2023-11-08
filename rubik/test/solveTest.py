'''
Created on Sep 12, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solve as solve

class Test(unittest.TestCase):

# Analysis
#
#    inputs:
#        parms: dict; mandatory; arrives validated
#        parms['op']: string; 'solve', mandatory, arrives validated 
#        parms['cube']: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives unvalidated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: dict
#        nominal:
#            dict['rotations']: string, Directions to create white cross
#            dict['status']: 'ok'
#        abnormal:
#            dict['status']: 'error: xxx', where xxx is a nonempty developer-selected diagnostic
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube that is already solved
#        test 020: nominal valid cube with solved Top Face
#        test 030: nominal valid cube with solved Middle Layer
#        test 040: nominal valid cube that has a solved Bottom Layer
#        test 050: nominal valid cube that has a solved Bottom Cross
#        test 060: nominal valid cube with no start
#        test 070: nominal valid cube that has a daisy 
#        test 080: nominal valid cube that has a line on top and solved middle layer
#        test 090: nominal valid cube that has a l on top and a solved middle layer
#        test 100: nominal valid cube that has a cross on top and solved middle layer
#        test 110: nominal valid cube that has matching corners and has solved top face
#        test 120: nominal valid cube that caused an error in my submission
#        test 130: nominal valid cube but we check the token to make sure it is correct
#        test 140: nominal valid cube where white isn't on bottom
#        test 141: same as 140, but with another cube
#        test 150: detecting if the cube is actually solved
#        test 160: detecting if the cube will be solved from failing test case
#
#    sad path:
#        test 910: abnormal cube with invalid length
#        test 920: abnormal cube with invalid colors
#        test 930: abnormal cube with invalid middle colors
#        test 940: abnormal cube with invalid amount of colors
#        test 950: No cube presented
#        test 960: abnormal unsolvable cube with a corner turned
#        test 970: abnormal cube with swapped stickers
#        test 980: abnormal cube with multiple corners turned
#        test 990: abnormal cube that should be caught by initial check
#        test 9100: abnormal unsolvable cube that should be caught by initial check and bottom isn't white
#        test 9110: abnormal unsolvable cube and bottom isn't white


    def test_solve_010_ShouldReturnSolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_020_ShouldReturnSolvedCubeFromTopFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grbrrrrrrrggggggggoboooooooborbbbbbbyyyyyyyyywwwwwwwww'
        
        actualResult = solve._solve(inputDict)
        expectedRotations = 'bUFuBUUfUFUUfLLufBLLFbuLL'
            
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_030_ShouldReturnSolvedCubeFromSolvedMiddleLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gybrrrrrryygggggggyyyoooooobyybbbbbbrbrryoogowwwwwwwww'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'FURurURurfUUFURurfUURUrURUUrfUBuFUUbUBUUbLLufBLLFbuLL'
            
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
        
    def test_solve_040_ShouldReturnSolvedCubeFromSolvedBottomLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gobgrgrrryrrrggggggybyobooorbyobobbbybyryyoyowwwwwwwww'
        
        actualResult = solve._solve(inputDict)

        
        expectedRotations = 'UFUfuluLUBUburuRRUrufuFuRUrufuFLUlubuBuLUlubuBURRuFbRRfBuRR'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_050_ShouldReturnSolvedCubeFromSolvedBottomCross(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rywyggrgrbgbroogoowyggbrybowbybrrgryooroyygbobwwwwwywb'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'UURUrLUlluLUrURUUruRUUruRUBUbUfuFURUrluLUFUfULUlubuBUUFUfuluLUUFURurfURUrURUUruRUrURUUrlURuLUUrURUUrrULuRUUlULUUlBBURlBBrLUBBFFurLFFRluFF'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_060_ShouldReturnSolvedCubeFromNothing(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bgrbrgroygygwgbrbrobyrorgrwoywybwgobboygyoorywwbgwyoww'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'fUfUfuBBUUFFRRBBLLUUBUbubuBUURUrFufluLUUFUfuluLUURUrufuFbuBULUlUUruRUBUbFURurURurfUUFURurfRUrURUUrUURUrURUUrlURuLUUrURUUrUfUBuFUUbUBUUbRRUFbRRfBURR'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_070_ShouldReturnSolvedCubeFromDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ogyobbrobgobyryogwrbgoggbbbyrwrobwrwrwywywgwoggyywyorr'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'UUFFRRBBLLRUrULUluFUfUrURUUruRUbuBULUlBUburuRuluLUFUfRUrufuFuRUrufuFUFURurfuRUrURUUrURUrURUUruRUrURUUrUlURuLUUrURUURuFbRRfBuRR'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_080_ShouldReturnSolvedCubeFromlineOnTop(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grybbbbbboyorrrrrryobggggggryrooooooyygbygyybwwwwwwwww'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'FURurfUUFURurfuRUrURUUrUURUrURUUruRUrURUUrUUrULuRUUlULUUl'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_090_ShouldReturnSolvedCubeFromLOnTop(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yyyoooooooybbbbbbbrorrrrrrrgroggggggyyyyybggbwwwwwwwww'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'FURurfUURUrURUUrUURUrURUUrlURuLUUrURUUrUUlURuLUUrURUUrLLUfBLLFbULL'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_100_ShouldReturnSolvedCubeCrossOnTop(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yboooooooyorbbbbbbggrrrrrrryrbggggggbyyyyyoygwwwwwwwww'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'UURUrURUUrUURUrURUUrlURuLUUrURUUrUUlURuLUUrURUUrLLUfBLLFbULL'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_110_ShouldReturnSolvedCubeFromMatchingCorners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'grgggggggogooooooobbbbbbbbbrorrrrrrryyyyyyyyywwwwwwwww'
        
        actualResult = solve._solve(inputDict)
       
        expectedRotations = 'FFUrLFFRlUFF'
        self.assertEqual(expectedRotations, actualResult['rotations'])

        
        
    def test_solve_120_ShouldReturnSolvedCubeFromNothingUsingFailingCubes(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'orbrggrowwworrbrboyyrybrbygywyboyoogboggwobwryggbywwgw'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'BLBULRUUBUBBLLUFFRRUBBLulUULUluluLUURurUBUbfuFluLUFUfUUbuBULUlRUrufuFuRUrufuFUFURurfrULuRUUlULUUlBBURlBBrLUBBRRUFbRRfBURR'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])

        
        
    def test_solve_130_ShouldReturnTokenFromSolvingCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbbbbbbrorrrrrrrgrgggggggogoooooooyyyyyyyyywwwwwwwww'
        
        actualResult = solve._solve(inputDict)
        expectedResult = True
        actualKey = False
        
        if actualResult['token'] in 'd10d7141503bd5dc0c5beb03e68d168c2c4e5a5e90544f0037f1b955f907dff1':
            actualKey = True
        
            
        self.assertEqual(expectedResult, actualKey) 
        
    def test_solve_140_validCubeWhereWhiteIsntOnBottom(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gwrgorrowyrybwgobggwgorrroowywwyyyrbogobbyrbbwwbggobyy'
        
        actualResult = solve._solve(inputDict)

        expectedRotations = 'lUlUUBULLUFFRRUBBRurLUlUUfuFluLUrURUUruRUbuBULUlBUburuRufuFURUrUFUfuluLUFURurfUUFURurfURUrURUUruRUrURUUrfUBuFUUbUBUUBURlBBrLUBB'
        
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_141_validCubeWhereWhiteIsntOnBottom(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bogwgrobwygybwgrybogywbrwrygbrwybrggoybyorwwrwogorobyo'
        
        actualResult = solve._solve(inputDict)
        
        expectedRotations = 'URLBUrURRUBBLLUFFUURUruluLUULUlUruRUUbuBULUlluLUFUfruRUBUbURUrufuFuRUrURurURurURUUrUUlURuLUUrURUUrLLufBLLFbuLL'
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_150_detectingIfCubeIsSolved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbgrgwywoyyggobgrororwbbwyoyrrrrgboobbwwyowyrboygwywgg'
        
        actualResult = solve._solve(inputDict)
                
        expectedRotations = 'RFUlRRFFUURRUBBLLfuFUUruRULulUFUfbuBURUrufuFUBUburuRLUlubuBluLUFUfUluLUFUfUFURurfuRUrURurURurURUUrlURuLUUrURUUrubUFuBUUfUFUUfBBURlBBrLUBB'     
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        
    def test_solve_160_detectingIfCubeIsSolvedFromFailingTestCase(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wwbgwgoygwbwwobyoggoboyroorrrggryyyywyowbrrbobbrrgwbgy'
        
        actualResult = solve._solve(inputDict)
                
        expectedRotations = 'lRLbblUUBuFFRRBBLLfuFbuBUUluLUUBUbULUlubuBUruRUBUbRUrufuFluLUFUfUluLUFUfUFURurfUUFURurfRUrURUUrUrULuRUUlULUUlFFUrLFFRlUFF'     
                
        self.assertEqual(expectedRotations, actualResult['rotations'])
        


# Sad Path
    def test_solve_910_abnormalCubeWithInvalidLength(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oowgobroggbwrbrrbyrywyryorobgwogoygyogbryygbrbwywwwbwgggrroo'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must be exactly 54 characters'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_920_abnormalCubeWithInvalidColors(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbwoowyywrrybbrbbvggwrtwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must contain characters of brogwy meaning blue, red, orange, green, white, yellow'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_930_abnormalCubeWithInvalidNumberOfOccurances(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brbworryywrrybbrbbgggwrgwrgowooggoggygyoyyyrrrbbrwowwo'
        
        expectedResult = {}
        expectedResult['status'] = "error: invalid cube, there must be exactly 9 spaces of each color"
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solve_940_abnormalCubeWithInvalidMiddleColors(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbrbbbbrrrrrrbrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, rubik\'s cubes cannot contain two middle pieces of the same color'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_950_noCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = ''
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must present a cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_960_unsolvableCubeWithCornerTurned(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oyrwgbyybgwwooryywrggbbgoowowwyrrrwoyrbbyggryborowbggb'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_970_unsolvableCubeWithStickersSwapped(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'orywryygwogbogwgobrywooywrbgrggbbrorrbyyyrywbgwogwbwbo'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_980_unsolvableCubeWithMultipleCornersTurned(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yrywryygwogbogwgobrywooywrbgrogbbrorrbyyyrgwbgwogwbwbo'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_990_unsolvableCubeThatShouldBeCaughtByInitialCheck(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ryrwgbyybgwwooryywrggbbgoowowgyrrrwoyrbbygowyborowbggb'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_9100_unsolvableCubeThatShouldBeCaughtByInitialCheckWhereWhiteIsntBottomColor(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bwgwgroboygybwgrybogywbrwrygbrwybrggoybyorwwrwogorobyo'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_9110_unsolvableCubeWithTwistedCornerAndBottomIsntWhite(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wogwgrobwygybwgrybogywbrwrygbbwybrggoybyorrwrwogorobyo'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_9120_unsolvableCubeWithMultipleWhites(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ygobrbgroyoywgwbworwrgooywwwrrgbygbygobyybbygrgwrwoorb'
        
        expectedResult = {}
        expectedResult['status'] = 'error: unsolvable cube'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()