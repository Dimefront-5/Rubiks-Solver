'''
Created on Sep 12, 2022

@author: Tyler Ray
'''
import unittest
import rubik.solveBottomCross as solveBottomCross

class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#         cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
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
#        test 020: nominal valid cube with white cross
#        test 030: nominal valid cube that doesn't have a cross but has a daisy
#        test 040: nominal valid cube that has nothing
#        test 050: nominal valid cube where there is an collision in a specific spot
#        test 060: nominal valid cube where there is an collision in a specific spot
#
#    no sad path
#        I do not think it is possible to dynamically catch a unsolvable cube at this exact layer. 



    def test_solveBottomCross_010_ShouldReturnSolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = ''
        expectedResult['status'] = 'ok'
        
        actualResult = solveBottomCross._solveBottomCross(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
    def test_solveBottomCross_020_ShouldReturnSolvedCubeFromNothing(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royorbowgoooygryrwwowyowryyrrbgbwgrgbybgygybbwbowwbrgg'
        
        expectedResult = {}
        expectedResult['rotations'] = 'FlUUlUlULLUFFRRUBB'
        expectedResult['status'] = 'ok'
        
        actualResult = solveBottomCross._solveBottomCross(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
    def test_solveBottomCross_030_ShouldReturnSolvedCubeFromDaisy(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yogrrbggbrrbogowgbygryoyyyobbogbywrywwowywgwwrrobwogbr'
        
        expectedResult = {}
        expectedResult['rotations'] = 'LLUFFRRUBB'
        expectedResult['status'] = 'ok'
        
        actualResult = solveBottomCross._solveBottomCross(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_solveBottomCross_040_ShouldReturnSolvedCubeFromNothing(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ywoyrobwrggryybggbyrroorwgybygbwgorywwbbbrrbwoowygwgoo'
        
        expectedResult = {}
        expectedResult['rotations'] = 'RBfrUUUFFBBUULLUFFRR'
        expectedResult['status'] = 'ok'
        
        actualResult = solveBottomCross._solveBottomCross(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solveBottomCross_050_ShouldReturnSolvedCubeWeirdCornerCase(self):
        inputDict = {}
        inputDict['cube'] = 'owyygbyoggrboorrrbwggbbyywwwrbgrbrooowryywwbobgyywggor'
                
        actualResult = solveBottomCross._solveBottomCross(inputDict['cube'])
        
        expectedResult = {}                                                  
        expectedResult['rotations'] = 'FUURBUrRRUUBBUFFLL'
        
        self.assertEqual(expectedResult['rotations'], actualResult.get('rotations'))
        self.assertEqual('ok', actualResult.get('status'))
        
    def test_solveBottomCross_060_ShouldReturnSolvedCubeWeirdCornerCaseWhiteonBottomWhiteAbove(self):
        inputDict = {}
        inputDict['cube'] = 'orbbgyywowggborbrbwrrbbyywwgoygrorogyyogywbwrobwywggor'
                
        actualResult = solveBottomCross._solveBottomCross(inputDict['cube'])
        
        expectedResult = {}                                                  
        expectedResult['rotations'] = 'FlfBUrFFRRBBLL'
        
        self.assertEqual(expectedResult['rotations'], actualResult.get('rotations'))
        self.assertEqual('ok', actualResult.get('status'))
    
        
    

    
#100 _rotateToDiasy
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated,  
#    output
#        dict['cube']: A rotated cube based based on what is needed to turn
#        dict['dir']: A set of directions to get to the rotated cube
#        dict['status']: The status of the cube
#    Happy path analysis
#        test 010: nominal cube with turn on first face
#        test 020: nominal cube with turn on 4th face
#        test 030: nominal cube with turn that avoids moving a white space
#
#    Happy path

    def test_rotateToDiasy_110_turnonFirstFace(self):
        inputDict = {}
        inputDict['cube'] = 'yggwryoygyrwbgryywggwgoogbbbbrwbbrgbowrrywboryroywowoo'
        
        expectedResult = 'yggyrywygyrwbgryywggbgorgborbbbbgbwrywrwywoorbroowowoo'
        
        actualResult = solveBottomCross._rotatetoDaisy(inputDict['cube'], 3, 1)
        
        self.assertEqual(expectedResult, actualResult['cube'])
        self.assertEqual('l', actualResult['dir'])
        
    
    def test_rotateToDiasy_120_turnOnSecondFace(self):
        inputDict = {}
        inputDict['cube'] = 'wwogbroowybgbroryrwrbygwyyorgbgorbybywooywrogybgrwbwgg'
        
        
        actualResult = solveBottomCross._rotatetoDaisy(inputDict['cube'], 1, 0)
        
        self.assertEqual('FUUR', actualResult['dir'])
    
    def test_rotateToDiasy_130_turnOnFourthFaceandDontOverride(self):
        inputDict = {}
        inputDict['cube'] = 'brryryorygowgggogobwbwoywbwrbrobbrybyrooywwbyyggrwogwg'
        
        expectedResult = 'goyyrrorobgowggbgogbrooygbwbrrobbrybwowbywywrygwrwygwy'
        
        actualResult = solveBottomCross._rotatetoDaisy(inputDict['cube'], 21, 11)
        
        self.assertEqual(expectedResult, actualResult['cube'])
        self.assertEqual('Ur', actualResult['dir'])
        

        

#200 _move
#    confidence level: BVA
#    input-output analysis
#    input
#       inputDict: 'cube'; string, mandatory, validated 'dir'; string, mandatory, validated
#       topIndex: int, mandatory, validated
#       index: int, mandatory, validated
#    output
#        outputDict: 'cube'; string, mandatory, validated 'dir'; string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube without an collision
#        test 020: nominal cube with a collision
#
#
#    Happy path

        def test_move_210_withoutAnCollision(self):
            inputDict = {}
            inputDict['cube'] = 'rrowrggyobgyoggbboboyyobwrrgrwrbbgbyowryywbwyrowywowgg'
            inputDict['dir'] = 'l'
        
            expectedResult = {}
            expectedResult['cube'] = 'rroyrgwyobgyoggbbobobyoywrowbyrbbgrgrwywywrwgybrgwogow'
            expectedResult['dir'] ='l'
        
            actualResult = solveBottomCross._move(inputDict, 39, 4)
        
            self.assertEqual(expectedResult['cube'], actualResult['cube'])
            self.assertEqual(expectedResult['dir'], actualResult['dir'])

        
    def test_move_220_withAnCollision(self):
            inputDict = {}
            inputDict['cube'] = 'wgbwroyyrroybgygybobobogwgwyrbrbbgrrgrbwywrwygowywgooo'
            inputDict['dir'] = 'l'
            
            expectedResult = {}
            expectedResult['cube'] = 'grbyrooyrwgbbgygybrogborwgbobrbbrorgywywywywrwowgwgyoo'
            expectedResult['dir'] ='UUUl'
            
            actualResult = solveBottomCross._move(inputDict, 39, 3)
            
            self.assertEqual(expectedResult['dir'], actualResult['dir'])
            self.assertEqual(expectedResult['cube'], actualResult['cube'])
        
#300 _createDaisy
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       directions: string, mandatory, validated
#       bottomMiddleColor: char, mandatory, validated
#    output
#        outputDict: 'cube'; string, mandatory, validated 'dir'; string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube
#
#    Happy path        

        
    def test_createDaisy_310_nominalValidCube(self):
            inputDict = {}
            inputDict['cube'] = 'yrbwroyyrwgbbgygybroybogwgwoborbbgrrbwyrywgwrgowywgooo'
            
            expectedResult = 'grbyrooyrwgbbgygybrogborwgbobrbbrorgywywywywrwowgwgyoo'
            
            actualResult = solveBottomCross._rotatetoDaisy(inputDict['cube'], 3, 1)
            self.assertEqual(expectedResult, actualResult['cube'])
            self.assertEqual('l', actualResult['dir'])
        
#400 _flipDaisy
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       directions: string, mandatory, validated
#       bottomMiddleColor: char, mandatory, validated
#    output
#        outputDict: 'cube'; string, mandatory, validated 'dir'; string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube with rotation on first face
#        test 020: nominal cube where there needs to be a rotation to find a match
#
#    Happy path        

    def test_flipDaisy_410_nominalValidCube(self):
            cube = 'wgbbgygybrogborwgbobrbbrorggrbyrooyrywywywrwywgoowowgy'
            
            expectedResult = 'bygygbbgwrogoorbgbobrbbrorggrwyrboyrywywywogwywrowowgy'
            
            actualResult = solveBottomCross._flipDaisy(cube, 'w')
            
            self.assertEqual(expectedResult, actualResult['cube'])
            self.assertEqual('FF', actualResult['dir'])
        
    def test_flipDaisy_420_nominalValidCubeNeedsARotation(self):
            cube = 'grbbgygybwgbborworwgbrogbbrorgobryrooyrywywywywrwgoowowgy'
                    
            actualResult = solveBottomCross._flipDaisy(cube, 'w')
            
            self.assertEqual(0, actualResult['flip'])
            self.assertEqual('U', actualResult['dir']) 
              
        
#500 _determineFlip
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       index: int, mandatory, validated
#       bottomMiddleColor: char, mandatory, validated
#    output
#        outputDict: 'cube'; string, mandatory, validated 'dir'; string, mandatory, validated
#    Happy path analysis
#        test 010: nominal cube with a front rotation
#        test 020: nominal cube with a right rotation
#        test 030: nominal cube with a back rotation
#        test 040: nominal cube with a left rotation
#
#    Happy path  

    def test_determineFlip_510_nominalValidCubeFrontRotation(self):
            cube = 'wgbbgygybrogborwgbobrbbrorggrbyrooyrywywywrwywgoowowgy'
                    
            actualResult = solveBottomCross._determineFlip(cube, 1, 'w')
            
            self.assertEqual('FF', actualResult['dir'])
        
    def test_determineFlip_520_nominalValidCubeRightRotation(self):
            cube= 'bygygbbgwrogoorbgbobrbbrorggrwyrboyrywywywogwywrowowgy'
                    
            actualResult = solveBottomCross._determineFlip(cube, 10, 'w')
            
            self.assertEqual('RR', actualResult['dir'])
            
            
    def test_determineFlip_530_nominalValidCubeBackRotation(self):
            cube= 'byoygbbgobgbroogorwbrbbrgrggrwyrboyrywrwyoogyywyowwwgw'
                    
            actualResult = solveBottomCross._determineFlip(cube, 19, 'w')
            
            self.assertEqual('BB', actualResult['dir'])
    
    def test_determineFlip_540_nominalValidCubeLeftRotation(self):
            cube= 'byoygbbgobgoroygoggrgrbbrbwrrworbbyrwgwwyoogyywyowwrwy'
                    
            actualResult = solveBottomCross._determineFlip(cube, 28, 'w')
            
            self.assertEqual('LL', actualResult['dir'])
            
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()