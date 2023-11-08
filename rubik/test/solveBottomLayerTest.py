'''
Created on Sep 26, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solveBottomLayer as solveBottomLayer


class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#        cube string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: outputDict
#            outputDict['rotation']: string; the rotations performed on the cube to solve the bottom layer
#            outputDict['cube']: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; 
#
#    confidence level: boundary value analysis
#
#    happy path:
#       
#        test 010: nominal valid cube that has the bottom layer solved
#        test 020: nominal valid cube that only has bottom face solved
#        test 030: A already solved cube
#        test 040: nominal valid cube that has bottom and 1 side face solved
#        test 050: A valid cube with a different bottom middle color
#        test 060: nominal valid cube with whites only on top corners

    def test_solveBottomLayer_010_BottomLayerSolvedCube(self):
        
        cube = 'oorygygggybggrgrrrgoyroroooobrgbobbbbbyyyybrywwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['cube'] = 'oorygygggybggrgrrrgoyroroooobrgbobbbbbyyyybrywwwwwwwww'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
    def test_solveBottomLayer_020_BottomFaceSolved(self):
        
        cube = 'rrborbbrgyyyygyogrgbrooygobygyrbbrbobrooygggowwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'lULUbuBFUfRurUUUBUbfuF'
        expectedResult['cube'] = 'ogrbryrrrggyrgbgggboyyoboooggyobrbbboyroyybrywwwwwwwww'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomLayer_030_SolvedCube(self):
        
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomLayer_040_BottomSolvedCubeOneFace(self):
        
        cube = 'yoyoyygybgbgbgyyggwowgwwwwwbgbobbbbyogowowoyorrrrrrrrr'
        
        expectedResult = {}
        expectedResult['rotations'] = 'lULUUUfuFUUFUf'
        expectedResult['cube'] = 'wbgoybyyywgbogygggyyggwwwwwoyoobgbbbybooowbworrrrrrrrr'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
            
    def test_solveBottomLayer_050_SolveCubeDifferentBottomColor(self):
        
        cube = 'owrbyyyyrggwggowgbgboywowwwbbggbygbbywroowyoyrrbrrroro'
        
        expectedResult = {}
        expectedResult['rotations'] = 'fuFUUUbuBUUUrURUUruR'
        expectedResult['cube'] = 'ogobybyyyyowogygggbbbgwwwwwyowobybbbowoyoggwgrrrrrrrrr'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
    def test_solveBottomLayer_060_SolveCubeWithoutAnysquaresOnBottomCornersOrOnTop(self):
        
        cube = 'bgryrrrrbwygygooggobryoooorgbwgbbbbbyryoygorgwwywwwyww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'RUrbuB'
        expectedResult['cube'] = 'ygyyrrrrroygbgogggobryoyooogorgbbbbbyoygyrbrbwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomLayer_070_BrokeMyCodeCube(self):
        
        cube = 'wyybyyoyybrbrbgrbwyywrggrgrrbborogrbgowgoogbogwowwwowy'
        
        expectedResult = {}
        expectedResult['rotations'] = 'buBUUUBUbRurUUUFUfRurUURUr'
        expectedResult['cube'] = 'yyogyoyyygrgbbobbboryygrgggbbrororrrogbgoyobrwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomLayer(cube)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
     
    
        
# 200 _solveBottomFaceTopFaceCorners
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       bottomMiddleCube: char, mandatory, valid.
#    output
#        outputDict
#            outputDict['cube']: string, mandatory, validated
#            outputDict['rotations']: string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube with corner on top left corner
#        test 020: nominal cube with corner on top right corner
#        test 030: nominal cube with corner on bottom left corner
#        test 040: nominal cube with corner on bottom right corner
#        test 050: nominal cube with corner on top but needs a rotation to flip
#
#    Happy path     

    def test_solveBottomFaceTopCorners_210_WhitePieceOnTopLeftCorner(self):
        
        cube = 'ygyrrorrrrgbygygggrrbboboobooorbyobbwgybyogygwwwwwwyww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'Lul'
        expectedResult['cube'] = 'yrorrorrrwgyygygggrgbbogooyyoorbyrbboogbyygbbwwwwwwbww'
        actualResult = solveBottomLayer._solveBottomFaceTopFaceCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopCorners_220_WhitePieceOnTopRightCorner(self):
        
        cube = 'rgbygygggrrbboboobooorbyobbygyrrorrrgbwyyggoywwwwwwwwy'
        
        expectedResult = {}
        expectedResult['rotations'] = 'rUR'
        expectedResult['cube'] = 'bbbygygggrryboooooogybbygbbrgwrrorrrgyboygorywwwwwwwwy'
        actualResult = solveBottomLayer._solveBottomFaceTopFaceCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopCorners_230_WhitePieceOnBottomLeftCorner(self):
        
        cube = 'ooorbyobbygyrrorrrrgbygygggrrbboboobyoggyywbgywwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'lUL'
        expectedResult['cube'] = 'ogybbygbbrgwrrorrrbbbygygggrryboooooyrogyobygywwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopFaceCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopCorners_240_WhitePieceOBottomRightCorner(self):
        
        cube = 'rrbboboobooorbyobbygyrrorrrrgbygyggggygoybygwwwywwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'Rur'
        expectedResult['cube'] = 'rgbbogooyyoorbyrbbyrorrorrrwgyygygggbbgyybgoowwbwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopFaceCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
        
        
    def test_solveBottomFaceTopCorners_250_TopWhiteCornersWithRotation(self):
        
        cube = 'bbybrbrrrborogggggbyoroyoooyrogbrbbggowyygyyrywwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'U'
        expectedResult['cube'] = 'borbrbrrrbyoogggggyroroyooobbygbrbbgyygyyorgwywwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopFaceCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))

#300 _evaluateBottomLayer
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       bottomMiddleCube: char, mandatory, valid.
#    output
#        outputDict
#            outputDict['cube']: string, mandatory, validated
#            outputDict['rotations']: string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube with top face corners. no rotation needed to turn
#        test 020: White Piece on top corner
#        test 030: White Piece on Bottom Corner
#        test 040: Cube, that appears to be solved, but isn't
#
#    Happy path

    def test_evaluateBottomLayer_310_TopWhiteCornersWithRotation(self):
        
        cube = 'bbybrbrrrborogggggbyoroyoooyrogbrbbggowyygyyrywwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'UUlULUUluL'
        expectedResult['cube'] = 'gyoyrbrrryryogggggbooroyooobbrgbrbbbygryybyogwwwwwwwww'
        actualResult = solveBottomLayer._evaluateBottomLayer(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_evaluateBottomLayer_320_WhitePieceOnBackTopCorner(self):
        
        cube = 'yryboyooobobobybbywobgrborryrgrgygggogrgybryrwwwwwwwwg'
        
        expectedResult = {}
        expectedResult['rotations'] = 'BUb'
        expectedResult['cube'] = 'bogboyoooogrobgbbbgobrrbrrryryrgygggogyyyyrbywwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_evaluateBottomLayer_330_WhitePieceOnBottomCorner(self):
        
        cube = 'yybgrgrrrygbrgbggorryoobwoogygybobbbobyryyroowwwwwwwwg'
        
        expectedResult = {}
        expectedResult['rotations'] = 'rURBUb'
        expectedResult['cube'] = 'ygggrgrrrobrrgogggyygyoboooybbybobbbrrboyroyywwwwwwwww'
        actualResult = solveBottomLayer._evaluateBottomLayer(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_evaluateBottomLayer_340_appearsToBeSolvedCube(self):
        
        cube = 'rrborbbrgyyyygyogrgbrooygobygyrbbrbobrooygggowwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'lULUbuBFUfRurUUUBUbfuF'
        expectedResult['cube'] = 'ogrbryrrrggyrgbgggboyyoboooggyobrbbboyroyybrywwwwwwwww'
        actualResult = solveBottomLayer._evaluateBottomLayer(cube, 'w')
        
        self.assertEqual(expectedResult['rotations'], actualResult.get('rotations'))
        self.assertEqual(expectedResult['cube'], actualResult.get('cube'))
        
     
#400 _solveBottomFaceCorners
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       bottomMiddleCube: char, mandatory, valid.
#    output
#        outputDict
#            outputDict['cube']: string, mandatory, validated
#            outputDict['rotations']: string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube with corner on front face bottom left corner
#        test 020: nominal cube with corner on right face bottom left corner
#        test 030: nominal cube with corner on back face bottom left corner
#        test 040: nominal cube with corner on left face bottom left corner
#        test 050: nominal cube with corner on front face bottom right corner
#        test 060: nominal cube with corner on right face bottom right corner
#        test 070: nominal cube with corner on back face bottom right corner
#        test 080: nominal cube with corner on left face bottom right corner
#
#    Happy path  

    def test_solveBottomFaceCorners_410_WhitePieceOnBottomCornerFront(self):
        
        cube = 'rryoobwoogygybobbbyybgrgrrrygbrgbggoooryyrybogwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'lUL'
        expectedResult['cube'] = 'wygboboooyyyybobbbbbbgrgrrryggrgrggyooryyoorrgwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
        
    def test_solveBottomFaceCorners_420_WhitePieceOnBottomCornerRight(self):
        
        cube = 'ygbrgbggorryoobwoogygybobbbyybgrgrrrrrooyboyywwgwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'fUF'
        expectedResult['cube'] = 'yggrgrggywygboboooyyyybobbbbbbgrgrrrroroyroyowwgwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube')) 
        
    def test_solveBottomFaceCorners_430_WhitePieceOnBottomCornerBack(self):
        
        cube = 'yybgrgrrrygbrgbggorryoobwoogygybobbbobyryyroowwwwwwwwg'
        
        expectedResult = {}
        expectedResult['rotations'] = 'rUR'
        expectedResult['cube'] = 'bbbgrgrrryggrgrggywygboboooyyyybobbbrrooyyroowwwwwwwwg'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube')) 
    
    def test_solveBottomFaceCorners_440_WhitePieceOnBottomCornerLeft(self):
        
        cube = 'gygybobbbyybgrgrrrygbrgbggorryoobwooyyobyoorrwwwwwwgww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'bUB'
        expectedResult['cube'] = 'yyyybobbbbbbgrgrrryggrgrggywygbobooooyoryororwwwwwwgww'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube')) 
        
    def test_solveBottomFaceCorners_450_WhitePieceOnBottomCornerFrontRight(self):
        
        cube = 'oggygyggwyyyoobgooggbobrbbbryybrgrrryoobyrbrrwwowwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'Rur'
        expectedResult['cube'] = 'rywygrggboyygobooogoyobrbbbrgbbrgrrrgyooyrybgwwywwwwww'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceCorners_460_WhitePieceOnBottomCornerRightRight(self):
        
        cube = 'ryybrgrrroggygyggwyyyoobgooggbobrbbborroyrybbwwwwwwwwo'
        
        expectedResult = {}
        expectedResult['rotations'] = 'Bub'
        expectedResult['cube'] = 'rgbbrgrrrrywygrggboyygobooogoyobrbbborgyybgoywwwwwwwwy'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceCorners_470_WhitePieceOnBottomCornerBackRight(self):
        
        cube = 'ggbobrbbbryybrgrrroggygyggwyyyoobgoorrbrybooywwwwwwoww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'Lul'
        expectedResult['cube'] = 'goyobrbbbrgbbrgrrrrywygrggboyygobooogbyryooygwwwwwwyww'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceCorners_480_WhitePieceOnBottomCornerLeftRight(self):
        
        cube = 'yyyoobgooggbobrbbbryybrgrrroggygyggwbbyryorroowwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'Fuf'
        expectedResult['cube'] = 'oyygobooogoyobrbbbrgbbrgrrrrywygrggbyogbyygroywwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceBottomCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
    
# 500 _solveBottomFaceTopSidesCorners
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       bottomMiddleCube: char, mandatory, valid.
#    output
#        outputDict
#            outputDict['cube']: string, mandatory, validated
#            outputDict['rotations']: string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube with corner on front face top left corner
#        test 020: nominal cube with corner on right face top left corner
#        test 030: nominal cube with corner on back face top left corner
#        test 040: nominal cube with corner on left face top left corner
#        test 050: nominal cube with corner on front face top right corner
#        test 060: nominal cube with corner on right face top right corner
#        test 070: nominal cube with corner on back face top right corner
#        test 080: nominal cube with corner on left face top right corner
#
#    Happy path     

    def test_solveBottomFaceTopSidesCorners_510_WhitePieceOnFrontTopLeftCorner(self):
        
        cube = 'wobgrborryrgrgygggyryboyooobobobybbyryrbygrgogwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'FUf'
        expectedResult['cube'] = 'gobrrbrrryryrgygggbogboyoooogrobgbbbybryyyygowwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))

    def test_solveBottomFaceTopSidesCorners_520_WhitePieceOnRightTopLeftCorner(self):
        
        cube = 'bobobybbywobgrborryrgrgygggyryboyooorgoyygrbrwwgwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'RUr'
        expectedResult['cube'] = 'ogrobgbbbgobrrbrrryryrgygggbogboyoooryobygyyywwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopSidesCorners_530_WhitePieceOnBackTopLeftCorner(self):
        
        cube = 'yryboyooobobobybbywobgrborryrgrgygggogrgybryrwwwwwwwwg'
        
        expectedResult = {}
        expectedResult['rotations'] = 'BUb'
        expectedResult['cube'] = 'bogboyoooogrobgbbbgobrrbrrryryrgygggogyyyyrbywwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopSidesCorners_540_WhitePieceOnLeftTopLeftCorner(self):
        
        cube = 'yrgrgygggyryboyooobobobybbywobgrborrrbrgyyogrwwwwwwgww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'LUl'
        expectedResult['cube'] = 'yryrgygggbogboyoooogrobgbbbgobrrbrrryyygyboyrwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
         
    def test_solveBottomFaceTopSidesCorners_550_WhitePieceOnFrontTopRightCorner(self):
        
        cube = 'rgwobgbbyrorrrbbrryggrgygggoyyboyoooyobrybgybwwowwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'fuF'
        expectedResult['cube'] = 'rgoobybbbygyrrbrrroorrgygggygyboyooobbboyrgygwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopSidesCorners_560_WhitePieceOnRightTopRightCorner(self):
        
        cube = 'oyyboyooorgwobgbbyrorrrbbrryggrgygggbbboyyyrgwwwwwwwwo'
        
        expectedResult = {}
        expectedResult['rotations'] = 'ruR'
        expectedResult['cube'] = 'ygyboyooorgoobybbbygyrrbrrroorrgygggbrgbyybogwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopSidesCorners_570_WhitePieceOnBackTopRightCorner(self):
        
        cube = 'yggrgygggoyyboyooorgwobgbbyrorrrbbrrbygbyrboywwwwwwoww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'buB'
        expectedResult['cube'] = 'oorrgygggygyboyooorgoobybbbygyrrbrrrgygryobbbwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
    def test_solveBottomFaceTopSidesCorners_580_WhitePieceOnLeftTopRightCorner(self):
        
        cube = 'rorrrbbrryggrgygggoyyboyooorgwobgbbygryyyobbbowwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'luL'
        expectedResult['cube'] = 'ygyrrbrrroorrgygggygyboyooorgoobybbbgobyybgrbwwwwwwwww'
        actualResult = solveBottomLayer._solveBottomFaceTopSidesCorners(cube, 'w')
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('dir'))
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()