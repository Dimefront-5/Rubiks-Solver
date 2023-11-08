'''
Created on Sep 13, 2022

@author: tman1
'''
import unittest
import rubik.validation as validation


class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#        parms: dict; mandatory; arrives validated
#        parms['cube']: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives unvalidated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: string
#        nominal:
#            String : 'ok'
#        abnormal:
#            String: 'error: xxx', where xxx is a nonempty developer-selected diagnostic
#
#    confidence level: boundary value analysis
#
#    happy path:
#        test 010: nominal cube
#
#    sad path:
#
#        test 910: abnormal cube with a invalid length
#        test 920: abnormal cube with invalid colors
#        test 930: abnormal cube with an incorrect number of each color
#        test 940: no cube presented
#        test 950: abnormal cube with incorrect middle colors

    def test_validationTest_010_nominalCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        expectedResult = {}
        expectedResult['status'] = 'ok'
        
        actualResult = validation._validation(inputDict['cube'])
  
        self.assertEqual(expectedResult.get('status'), actualResult)
        
# Sad Path
    
    def test_validationTest_910_invalidCubeLength(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywww'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must be exactly 54 characters'
        
        actualResult = validation._validation(inputDict['cube'])
  
        self.assertEqual(expectedResult.get('status'), actualResult)
        
    def test_validationTest_920_invalidCubeColors(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrggtggggggooojoooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must contain characters of brogwy meaning blue, red, orange, green, white, yellow'
        
        actualResult = validation._validation(inputDict['cube'])
  
        self.assertEqual(expectedResult.get('status'), actualResult)
    
    def test_validationTest_930_invalidNumberofColors(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrbbbbrrrrrrbrrggggrgrggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, there must be exactly 9 spaces of each color'
        
        actualResult = validation._validation(inputDict['cube'])
  
        self.assertEqual(expectedResult.get('status'), actualResult)
    
    def test_validationTest_940_noCubePresented(self):
        inputDict = {}
        cube = None
        expectedResult = {}
        expectedResult['status'] = 'error: invalid cube, must present a cube'
        
        actualResult = validation._validation(cube)
  
        self.assertEqual(expectedResult.get('status'), actualResult)
        
    def test_validationTest_950_incorrectMiddleColors(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['status'] = "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
        
        actualResult = validation._validation(inputDict['cube'])
  
        self.assertEqual(expectedResult.get('status'), actualResult)
        
    #1300 _cubeValidity
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, unvalidated,  
    #    output
    #        an error code if it's invalid, ok if it is valid.
    #    Happy path analysis
    #        test 010: nominal cube
    #    Sad Path analysis
    #        test 910: No cube presented
    #        test 920: Length is invalid
    #        test 930: invalid colors
    #        test 940: Invalid middle colors
    #        test 950: invalid number of colors.
    #Happy path
    
    def test_validation_1310_ValidNomianlCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._cubeValidity(inputDict['cube'])
        
        self.assertEqual('ok', actualResult) 
        
    #sad path
    
    def test_validation_13910_NoCube(self):
        inputDict = {}
        inputDict['cube'] = None
        
        actualResult = validation._cubeValidity(inputDict['cube'])
        
        self.assertEqual('error: invalid cube, must present a cube', actualResult) 
    
    def test_validation_13920_InvalidLength(self):
        inputDict = {}
        inputDict['cube'] = 'gggggg'
        
        actualResult = validation._cubeValidity(inputDict['cube'])
        
        self.assertEqual('error: invalid cube, must be exactly 54 characters', actualResult)
        
    def test_validation_13930_InvalidColorNames(self):
        inputDict = {}
        inputDict['cube'] = 'bbbwoowyywrrybbrvbgggwrgwrtowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._cubeValidity(inputDict['cube'])
        
        self.assertEqual('error: invalid cube, must contain characters of brogwy meaning blue, red, orange, green, white, yellow', actualResult)
        
    def test_validation_13940_InvalidMiddleBoxes(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrbbbbrrrrrrbrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        actualResult = validation._cubeValidity(inputDict['cube'])
        
        self.assertEqual("error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color", actualResult)
        
    def test_validation_13950_InvalidNumberOfColors(self):
        inputDict = {}
        inputDict['cube'] = 'rrbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._cubeValidity(inputDict['cube'])
        
        self.assertEqual("error: invalid cube, there must be exactly 9 spaces of each color", actualResult)
        
        
    #1400 _colorCount
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated. 
    #    output
    #        an error code if it's invalid and has too many colors, ok if it is valid.
    #    Happy path analysis
    #        test 010: nominal cube
    #    Sad Path analysis
    #        test 910: Invalid number of colors
    #Happy path
    
    def test_validation_1410_ValidNomianlCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._colorCount(inputDict['cube'])
        
        self.assertEqual(None, actualResult) 
        
    #sad path
    
    def test_validation_14910_invalidNumberofColors(self):
        inputDict = {}
        inputDict['cube'] = 'rrbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._colorCount(inputDict['cube'])
        
        self.assertEqual("error: invalid cube, there must be exactly 9 spaces of each color" , actualResult) 
        
        
    #1500 _validMiddleCubes
    #    confidence level: BVA
    #    input-output analysis
    #    input
    #       cube: string, mandatory, validated. 
    #    output
    #        an error code if it's invalid and has too many middles spaces, ok if it is valid.
    #    Happy path analysis
    #        test 010: nominal cube
    #    Sad Path analysis
    #        test 910: Invalid number of middle colors
    #Happy path
    
    def test_validation_1510_ValidNomianlCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbbwoowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._validMiddleCubes(inputDict['cube'])
        
        self.assertEqual(None, actualResult) 
        
    #sad path
    
    def test_validation_15910_invalidNumberofMiddleColors(self):
        inputDict = {}
        inputDict['cube'] = 'rrbwrowyywrrybbrbbgggwrgwrgowooggoggyyyoyyyrrrbbrwowwo'
        
        actualResult = validation._validMiddleCubes(inputDict['cube'])
        
        self.assertEqual("error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color" , actualResult)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()