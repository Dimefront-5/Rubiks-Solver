'''
Created on Oct 23, 2022

@author: Tyler Ray
'''
import unittest
import rubik.validTopCross as validTopCross

class Test(unittest.TestCase):
# Analysis
#
#    inputs:
#        cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives validated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: boolean
#        True: if cube's top cross is solved
#        False: if cube's top cross isn't solved
#
#    confidence level: boundary value analysis
#
#    happy path:
#       
#        test 010: nominal valid cube that has the top cross solved
#        test 011: test 010, with another cube
#        test 020: nominal valid cube that doesn't have the top cross solved but has an straight line
#        test 021: test 020, with another cube
#        test 030: nominal valid cube that has part of the top cross solved but has an l
#        test 031: test 030, with another cube
#

    def test_solve_010_ShouldReturnTrueFromTopCrossSolved(self):
        cube = 'yryrrrrrrbgoggggggybyoooooooogbbbbbbbygyyyryrwwwwwwwww'
        
        expectedResult = True
       
        
        actualResult = validTopCross._validTopCross(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_011_ShouldReturnTrueFromTopCrossSolved(self):
        cube = 'yryrrrrrrrgoggggggybyoooooooogbbbbbbbygyyybyrwwwwwwwww'
        
        expectedResult = True
       
        
        actualResult = validTopCross._validTopCross(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_020_ShouldReturnFalseFromLine(self):
        cube = 'gbyggggggbyoooooooygobbbbbbbyrrrrrrryygoyryyrwwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopCross._validTopCross(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_021_ShouldReturnFalseFromLine(self):
        cube = 'gbyggggggbyoooooooygobbbbbbbyrrrrrrryygryyyorwwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopCross._validTopCross(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_030_ShouldReturnFalseFromL(self):
        cube = 'byygggggggyrooooooyrrbbbbbbggorrrrrryybyyoybowwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopCross._validTopCross(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solve_031_ShouldReturnFalseFromL(self):
        cube = 'byygggggggyrooooooyrrbbbbbbggorrrrrryobyyybyowwwwwwwww'
        
        expectedResult = False
       
        
        actualResult = validTopCross._validTopCross(cube)
        
        self.assertEqual(expectedResult, actualResult)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()