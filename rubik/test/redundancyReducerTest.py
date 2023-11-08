'''
Created on Oct 11, 2022

@author: Tyler Ray
'''
import unittest
import rubik.redundancyReducer as redundancyReducer


class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#        rotations: string, validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: rotations
#        nominal: A string that has removed redundant turns. 
#
#    confidence level: boundary value analysis
#
#    happy path:
#        test 010: directions that aren't redundant
#        test 020: directions that have 1 redundancy
#        test 030: directions that are very redundant
#        test 040: all Redundant U directions
#        test 050: all Redundant F directions
#        test 060: all Redundant R directions
#        test 070: all Redundant B directions
#        test 080: all Redundant L directions
#        test 090: all Redundant D directions

# ----- Happy Path

    def test_redundancyReducer_010_ANonRedundantDirections(self):
        initialRotations = 'LLFFRRBB'
        
        
        expectedRotations = 'LLFFRRBB'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
        
    def test_redundancyReducer_020_1RedundantDirections(self):
        initialRotations = 'UUUFFRRBBLL'
        
        
        expectedRotations = 'uFFRRBBLL'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
        
    def test_redundancyReducer_030_MultipleRedundantDirections(self):
        initialRotations = 'ruRbUBLUlFufluLUUFUfuluLuruRUBUbUUULUlubuBUUURUrufuF'
        
        
        expectedRotations = 'ruRbUBLUlFufluLUUFUfuluLuruRUBUbuLUlubuBuRUrufuF'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_redundancyReducer_040_MultipleRedundantDirectionsForU(self):
        initialRotations = 'UUUUUuuUuuuuuuuuuUUuU'
        
        
        expectedRotations = 'U'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_redundancyReducer_050_MultipleRedundantDirectionsForF(self):
        initialRotations = 'FFFF ffff FFF fff ffFF FFff fF Ff'
        
        
        expectedRotations = 'fF'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_redundancyReducer_060_MultipleRedundantDirectionsForR(self):
        initialRotations = 'RRRRrrrrRRRrrrRrrR'
        
        
        expectedRotations = 'Rr'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
        
    def test_redundancyReducer_070_MultipleRedundantDirectionsForB(self):
        initialRotations = 'BBBB bbbb BBB bbb bbBB BBbb bB Bb'
        
        
        expectedRotations = 'bB'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
        
    def test_redundancyReducer_080_MultipleRedundantDirectionsForB(self):
        initialRotations = 'LLLL llll LLL lll llLL LLll lL Ll'
        
        
        expectedRotations = 'lL'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)
        
        
    def test_redundancyReducer_090_MultipleRedundantDirectionsForB(self):
        initialRotations = 'DDDD dddd DDD ddd ddDD DDdd dD Dd'
        
        
        expectedRotations = 'dD'
        
        actualRotations = redundancyReducer._redundancyReducer(initialRotations)
        
        self.assertEqual(expectedRotations, actualRotations)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()