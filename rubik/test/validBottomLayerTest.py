'''
Created on Sep 26, 2022

@author: Tyler Ray
'''
import unittest
import rubik.validBottomLayer as validBottomLayer

class Test(unittest.TestCase):

# Analysis
#
#    inputs:
#        cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: boolean
#        True: if cube's bottom layer is solved
#        False: if cube's bottom layer isn't solved
#
#    confidence level: boundary value analysis
#
#    happy path:
#       
#        test 010: nominal valid cube that has the bottom layer solved
#        test 011: test 010, with another cube
#        test 020: nominal valid cube that only has bottom face solved
#        test 021: test 020, with a different cube
#        test 030: nominal valid cube that has bottom and 1 side face solved
#        test 031: test 030, with a different cube
#        (Upon creating cubes, I have figured out that a cube can only have 1 side face solved for the bottom layer, or all of them)
#        test 040: A already solved cube
#

        def test_validBottomLayer_010_ShouldReturnTrueFromBottomCross(self):
            
            cube = 'oorygygggybggrgrrrgoyroroooobrgbobbbbbyyyybrywwwwwwwww'
        
            expectedResult = True
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult)
            
        def test_validBottomLayer_011_ShouldReturnTrueFromBottomCross(self):
            
            cube = 'rbygbybbboyobrrrrryyrggrgggyoyyooooobogbyggrbwwwwwwwww'
        
            expectedResult = True
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult)         
            
        def test_validBottomLayer_020_ShouldReturnFalseFromOnlyBottomFaceSolved(self):
            
            cube = 'gobrrgbrbryyrgyrgrgybroygogyorobboboobogygybywwwwwwwww'
        
            expectedResult = False
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult)
            
        def test_validBottomLayer_021_ShouldReturnFalseFromOnlyBottomFaceSolved(self):
            
            cube = 'oyyrgbbgrryyooggobbggobyrbgobygryoroyrrrybbogwwwwwwwww'
        
            expectedResult = False
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult)
            
        def test_validBottomLayer_030_ShouldReturnFalseFromOnlyBottomFaceandOneFaceSolved(self):
            
            cube = 'ybybrgrrrbggygoggoyoygoyboggybrbrobboyrbyroorwwwwwwwww'
        
            expectedResult = False
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult) 
            
        def test_validBottomLayer_031_ShouldReturnFalseFromOnlyBottomFaceandOneFaceSolved(self):
            
            cube = 'yyoorrgrbybgggyrggyrbgoyooorbbobgbbryyroyrobgwwwwwwwww'
        
            expectedResult = False
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult) 
        
        def test_validBottomLayer_040_ShouldReturnTrueFromSolvedCube(self):
            
            cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
            expectedResult = True
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult) 
        
        
        def test_validBottomLayer_041_ShouldReturnTrueFromSolvedCube(self):
            
            cube = 'bbbbbbbbbwwwwwwwwwooooooooogggggggggyyyyyyyyyrrrrrrrrr'
        
            expectedResult = True
        
            actualResult = validBottomLayer._validBottomLayer(cube)
        
            self.assertEqual(expectedResult, actualResult) 
        
        
        