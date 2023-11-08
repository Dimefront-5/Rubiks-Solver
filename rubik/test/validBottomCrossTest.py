'''
Created on Sep 30, 2022

@author: tyler
'''
import unittest
import rubik.validBottomCross as validBottomCross

class Test(unittest.TestCase):


#100 _isSidesValid
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, unvalidated,  
#    output
#        boolean: true if sides match with middle face color, o/w false
#    Happy path analysis
#        test 010: nominal cube
#    Sad path analysis
#        test 910: cube with no sides valid
#        test 920: cube with 3 sides valid
#        test 930: cube with 2 valid
#        test 940: cube with 1 valid
#
#    Happy path
    
    def test_isSidesValid_110_validCrossCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbgyrywrbwyyrgbygyggbyobgoyogrrbgbbgwrooyowoorwrwwwowr'
        
        expectedResult = True
        
        actualResult = validBottomCross._isSidesValid(inputDict['cube'])
        
        self.assertEqual(expectedResult, actualResult)
        
#    Sad path
    def test_isSidesValid_910_invalidCrossCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbgyrywbbwyyrgbyryggbyobggyogrrbgbrgwrooyowoorwrwwwowr'
        
        expectedResult = False
        
        actualResult = validBottomCross._isSidesValid(inputDict['cube'])
        
        self.assertEqual(expectedResult, actualResult)

#200 _isCrossValid
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, unvalidated,  
#    output
#        boolean: true if there is a cross on bottom, o/w false
#    Happy path analysis
#        test 010: nominal cube
#        test 020: cube with no cross
#
#    Happy path

    def test_isSidesValid_210_validCrossCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbgyrywrbwyyrgbygyggbyobgoyogrrbgbbgwrooyowoorwrwwwowr'
        
        expectedResult = True
        
        actualResult = validBottomCross._isCrossValid(inputDict['cube'], 'w')
        
        self.assertEqual(expectedResult, actualResult)

    def test_isSidesValid_220_invalidCrossCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbgyrywrbwyyrgbygyggbyobgoyogrrbgbbgwrooyowoorgrrwwowr'
        
        expectedResult = False
        
        actualResult = validBottomCross._isCrossValid(inputDict['cube'], 'w')
        
        self.assertEqual(expectedResult, actualResult)
        
        
#300 _isDaisyValid
#    confidence level: BVA
#    input-output analysis
#    input
#       cube: string, mandatory, validated
#       bottomMiddleColor: char, mandatory, validated
#    output
#        Boolean: True if there is an daisy, false if not
#    Happy path analysis
#        test 010: nominal cube without an daisy
#        test 020: nominal cube with an daisy
#
#    Happy path

    def test_isDaisyValid_310__validDaisyCube(self):
        inputDict = {}
        inputDict['cube'] = 'rrorbbgrgbgyyrgwyoboboggbbowbyyoywrorwywywrwgggyowbwor'
        
        expectedResult = True
        
        actualResult = validBottomCross._isDaisyValid(inputDict['cube'], 'w')
        
        self.assertEqual(expectedResult, actualResult)

    def test_isDaisyValid_320_invalidDaisyCube(self):
        inputDict = {}
        inputDict['cube'] = 'bbgyrywrbwyyrgbygyggbyobgoyogrrbgbbgwrooyowoorgrrwwowr'
        
        expectedResult = False
        
        actualResult = validBottomCross._isDaisyValid(inputDict['cube'], 'w')
        
        self.assertEqual(expectedResult, actualResult)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()