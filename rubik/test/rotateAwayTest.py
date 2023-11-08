'''
Created on Oct 10, 2022

@author: Tyler Ray
'''
import unittest
import rubik.rotateAway as rotateAway

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
#        test 010: cube that needs to be rotated to the right from front
#        test 010: cube that needs to be rotated to the right from right
#        test 010: cube that needs to be rotated to the right from back
#        test 010: cube that needs to be rotated to the right from left
#        test 050: cube that needs to be rotated to the left from front
#        test 060: cube that needs to be rotated to the left from right
#        test 070: cube that needs to be rotated to the left from back
#        test 080: cube that needs to be rotated to the left from left

# ----- Happy Path

    def test_rotateAway_010_cubeThatNeedsToBeRotatedToTheRightFromFront(self):
        cube = 'yrygrrrrroyoggggggyyyoooooorrrbbybbbgogyybbbbwwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'uluLUFUf'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 1)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test_rotateAway_020_cubeThatNeedsToBeRotatedToTheRightFromRight(self):
        cube = 'yyyrryrrrrgyggggggbybooooooyoobbbbbborryyrgbgwwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'ufuFURUr'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 10)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test_rotateAway_030_cubeThatNeedsToBeRotatedToTheRightFromBack(self):
        cube = 'yoobbbbbbyyyrryrrrrgyggggggbyboooooorrgryboygwwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'uruRUBUb'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 19)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test_rotateAway_040_cubeThatNeedsToBeRotatedToTheRight(self):
        cube = 'bybooooooyoobbbbbbyyyrryrrrrgygggggggbgryyrrowwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'ubuBULUl'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 28)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test_rotateAway_050_cubeThatNeedsToBeRotatedToTheLeftFromFront(self):
        cube = 'oryrrgrrrgogygggggybrooooooyrybbbbbbbyryyybgowwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'URUrufuF'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 1)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
        
    def test_rotateAway_060_cubeThatNeedsToBeRotatedToTheLeftFromRight(self):
        cube = 'yrrbbbbbbyrbrryrrryogbgggggoygooooooyyogygrybwwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'UBUburuR'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 10)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test_rotateAway_070_cubeThatNeedsToBeRotatedToTheLeftFromBack(self):
        cube = 'oygooooooyrrbbbbbbyrbrryrrryogbgggggogbyyyygrwwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'ULUlubuB'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 19)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))
        
    def test_rotateAway_080_cubeThatNeedsToBeRotatedToTheLeftFromLeft(self):
        cube = 'yogbgggggoygooooooyrrbbbbbbyrbrryrrrbyrgygoyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['rotations'] = 'UFUfuluL'
        expectedResult['status'] = 'ok'
        
        actualResult = rotateAway._rotateAway(cube, 28)
        
        self.assertEqual(expectedResult.get('rotations'), actualResult.get('rotations'))