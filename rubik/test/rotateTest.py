'''
Created on Aug 30, 2022

@author: Tyler Ray
'''
import unittest
import rubik.rotate as rotate

class Test(unittest.TestCase):

# Analysis
#
#    inputs:
#        parms: dict; mandatory; arrives validated
#        parms['op']: string; 'rotate', mandatory, arrives validated 
#        parms['cube']: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives unvalidated
#        parms['dir']: string; len .GE. 0, [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: dict
#        nominal:
#            dict['cube']: string, valid cube
#            dict['status']: 'ok'
#        abnormal:
#            dict['status']: 'error: xxx', where xxx is a nonempty developer-selected diagnostic
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube with no given rotation
#        test 020: nominal valid cube with multiple rotations
#        test 030: nominal valid cube with missing 'dir' key
#        test 040: nominal valid cube with one rotation
#
#    sad path:
#        test 910: missing cube, valid rotation
#        test 920: valid cube, with invalid rotation
#        test 930: invalid cube, not correct colors
#        test 940: Not colors in valid locations
#        test 950: Invalid Length
#        test 960: Uneven amount of colors

    def test_rotate_010_ShouldRotateValidNominalCubeWithoutDir(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        inputDict['dir'] = ''
        
        expectedResult = {}
        expectedResult['cube'] = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))  
        
    def test_rotate_020_ShouldRotateValidNominalCubeWithMultipleRotations(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'oorwrogbroborwgbwgygoogobybgrywybrgbwwgbbyrywwgwyoryry'
        inputDict['dir'] = 'RBFRUDFfLrBLDFlRBDRUlbBLr'
        
        expectedResult = {}
        expectedResult['cube'] = 'ogborrbgwyogowoobrybbggwoyowgwrywgrrgwbwbygyrwbrboyyry'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
             
    def test_rotate_030_ShouldRotateValidNominalCubeWithNoDir(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        expectedResult = {}
        expectedResult['cube'] = 'wwbyobyobyrrrbbrbbgggwrgwrgowrogbogbyyyoyyggorywrwowwo'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_rotate_040_ShouldRotateValidNominalCubeWithOneRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['cube'] = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        expectedResult['status'] = 'ok'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))  
    
    #sad path
    
    def test_rotate_910_MissingCube(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must present a cube'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotate_920_InvalidRotation(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        inputDict['dir'] = 'w'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid rotation, must be a rotation of F,f,R,r,B,b,L,l,U,u,D,d'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
        
    def test_rotate_930_InvalidColors(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbwoowyywrrybbrbbvggwrtwrgowooggoggyyyoyyyrrrbbrwowwo'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must contain characters of brogwy meaning blue, red, orange, green, white, yellow'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotate_940_InvalidMiddle(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'bbbwwooyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, rubik\'s cubes cannot contain two middle pieces of the same color'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

    def test_rotate_950_InvalidCubeLength(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'ggggg'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must be exactly 54 characters'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_rotate_960_InvalidCubeColors(self):
        inputDict = {}
        inputDict['op'] = 'rotate'
        inputDict['cube'] = 'brbworryywrrybbrbbgggwrgwrgowooggoggygyoyyyrrrbbrwowwo'
        inputDict['dir'] = 'F'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, there must be exactly 9 spaces of each color'
        
        actualResult = rotate._rotate(inputDict)
        
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
    #100 _rotate_F
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_110_ShouldRotateValidNominalCubeWithFRotation(self):
        inputDict = {}
        inputDict['cube'] = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
        
        expectedResult = {}
        expectedResult['cube'] = 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo'
        
        actualResult = rotate._rotate_F(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
                
                
    #200 _rotate_f
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_210_ShouldRotateValidNominalCubeWithfRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'groooyboywgbgbygrowoyrrrgyrbwobgbgwyryroywwwbogrbwgwby'
        
        actualResult = rotate._rotate_f(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
         
    #300 _rotate_R
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_310_ShouldRotateValidNominalCubeWithRRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'bowoogyyybwwrbgoybooywrrryrbwobgggwrrygoyrybogggbwrwbw'
        
        actualResult = rotate._rotate_R(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
                
                
    #400 _rotate_r
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_410_ShouldRotateValidNominalCubeWithrRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'boroowyyobyogbrwwbyoygrrwyrbwobgggwrrygoyrybwgggbwrwbo'
        
        actualResult = rotate._rotate_r(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
        
    #500 _rotate_B
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path   
    
    def test_rotate_510_ShouldRotateValidNominalCubeWithBRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'bogooryyowgywbbbrwgrwyrorryrwoyggrwrbyooywyboggwbwgbbg'
        
        actualResult = rotate._rotate_B(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
         
         
    #600 _rotate_b
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_610_ShouldRotateValidNominalCubeWithbRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'bogooryyowgrwbybrryrrorywrgwwobggywrgbboywyboggwbwgoyb'
        
        actualResult = rotate._rotate_b(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
        
        
    #700 _rotate_L
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
        
    def test_rotate_710_ShouldRotateValidNominalCubeWithLRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'rogooryyowgbwbybrowowrrbgyggbbwgwrgoryrrywybobgwowgyby'
        
        actualResult = rotate._rotate_L(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
            
            
    #800 _rotate_l
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    def test_rotate_810_ShouldRotateValidNominalCubeWithlRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'gogborwyowgbwbybrowoyrrogyrogrwgwbbgbyroywyborgwrwgyby'
        
        actualResult = rotate._rotate_l(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)  
          
          
    #900 _rotate_U
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path   
    def test_rotate_910_ShouldRotateValidNominalCubeWithURotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'wgbooryyowoywbybrobworrrgyrbogbgggwryorbyyowrggwbwgwby'
        
        actualResult = rotate._rotate_U(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)   
             
             
    #1000 _rotate_u
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_1010_ShouldRotateValidNominalCubeWithuRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'bwoooryyobogwbybrowgbrrrgyrwoybgggwrrwoyybroyggwbwgwby'
        
        actualResult = rotate._rotate_u(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult) 
           
           
    #1100 _rotate_D
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_1110_ShouldRotateValidNominalCubeWithDRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'bogoorgwrwgbwbyyyowoyrrrbrobwobgggyrryroywybowbgbwgygw'
        
        actualResult = rotate._rotate_D(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)
            
            
    #1200 _rotate_d
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated,  
    #    output
    #        rotatedCube: string, clockwise rotation of cube
    #    Happy path analysis
    #        test 010: nominal cube
    #Happy path
    
    def test_rotate_1210_ShouldRotateValidNominalCubeWithdRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bogooryyowgbwbybrowoyrrrgyrbwobgggwrryroywyboggwbwgwby'
        
        expectedResult = {}
        expectedResult['cube'] = 'bogoorbrowgbwbygyrwoyrrrgwrbwobggyyoryroywybowgygwbgbw'
        
        actualResult = rotate._rotate_d(inputDict['cube'])
        
        self.assertEqual(expectedResult.get('cube'), actualResult)        
    
    
    #1700 _validDir
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       direction: string, mandatory, unvalidated. 
    #    output
    #        an error code if it's invalid, nothing if it is valid.
    #    Happy path analysis
    #        test 010: nominal cube with dir
    #        test 020: nominal cube without dir
    #
    #    Sad Path analysis
    #        test 910: Invalid dir
    #Happy path
    
    def test_rotate_1710_ValidNomianlCube(self):
        inputDict = {}
        inputDict['dir'] = 'f'
        
        actualResult = rotate._validDir(inputDict['dir'])
        
        self.assertEqual('f', actualResult) 
    
    def test_rotate_1720_ValidNomianlCube(self):        
        actualResult = rotate._validDir(None)
        
        self.assertEqual('F', actualResult) 
        
    #sad path
    
    def test_rotate_17910_ValidNomianlCube(self):
        inputDict = {}
        inputDict['dir'] = 'w'
        
        actualResult = rotate._validDir(inputDict['dir'])
        
        self.assertEqual('Invalid', actualResult) 
        
        
    #1800 _evaluateDir
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       direction: string, mandatory, validated. 
    #    output
    #        returns a rotated cube
    #    Happy path analysis
    #        test 010: nominal cube with direction
    #Happy path
    
    def test_rotate_1810_ValidNomianlCube(self):
        inputDict = {}
        inputDict['dir'] = 'd'
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = rotate._evaluateDir(inputDict['dir'], inputDict['cube'])
        
        expectedResult = 'bbbwoorbbwrrybbwrggggwrgoggowooggwyyyyyoyyyrrboobwwrrw'
        
        self.assertEqual(expectedResult, actualResult)
    
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()