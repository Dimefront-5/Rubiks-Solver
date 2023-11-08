'''
Created on Nov 8, 2022

@author: Tyler Ray
'''
import unittest
import rubik.unsolvableCubeDetection as unsolvableCubeDetection


# Analysis
#
#    inputs:
#        cube: string; len=54, [bgroyw], 9 occurrences of each character, unique middle color; mandatory; arrives unvalidated
#
#    outputs:
#        side-effects: non state changes; no external effects
#        returns: boolean
#        nominal:
#            False: The cube is solvable
#        abnormal:
#            True: The cube is unsolvable
#
#    confidence level: boundary value analysis
#
#    happy path:
#        
#        test 010: nominal valid cube that is solvable
#        test 011: test 010, but another cube
#
#    sad path:
#        
#        test 910: abnormal cube that has has a opposite side on the same cube on the front
#        test 920: abnormal cube that has opposite side but cube is on the back
#        test 930: abnormal cube with same side on left
#        test 940: abnormal cube with opposite on right
#        test 950: abnormal cube with opposite side on top
#        test 960: abnormal cube with same side on bottom
#        test 970: abnormal cube that has a same side on the same cube
#        
#
# Happy Path


class Test(unittest.TestCase):


    def test_unsolvableCubeDetection_010_ShouldReturnFalseFromValidCube(self):
        cube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = False
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_unsolvableCubeDetection_011_ShouldReturnFalseFromValidCube(self):
        
        cube = 'gobgrgrrryrrrggggggybyobooorbyobobbbybyryyoyowwwwwwwww'
        
        expectedResult = False
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
# ------ Sad Path
#Normal Cube: owgyrrrwowyrwgbyybgwwooryywrggbbgoowbgyryrybogobgwobbr


    def test_unsolvableCubeDetection_910_ShouldReturnTrueFromInvalidCube(self):
        #0 and 43 were swapped
        cube = 'ryrwgbyybgwwooryywrggbbgoowowgyrrrwoyrbbygowyborowbggb'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_unsolvableCubeDetection_920_ShouldReturnTrueFromInvalidCubeOnBack(self):
        
        cube = 'wyrwgbyybgwwooryywrggobgoowowbyrrrwoyrbbygoryborowbggb'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_unsolvableCubeDetection_930_ShouldReturnTrueFromInvalidFromSharingSameSidesOnLeft(self):
        
        cube = 'rggbbgoowowgyrrrwowyrwgbyybgwwooryywyrowybbrybwgbworob'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_unsolvableCubeDetection_940_ShouldReturnTrueFromInvalidFromSharingOppositeSidesOnRight(self):
        
        cube = 'owgyrrrwowyrwgryyrgwwooryywrggbbgoowbgyryrybogobgwobbr'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_unsolvableCubeDetection_950_ShouldReturnTrueFromInvalidFromSharingOppositeSidesOnTop(self):
        
        cube = 'owgyrrrwowyrwgbbybgwwooryywrggbbgoowygyryrybogobgwobbr'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_unsolvableCubeDetection_960_ShouldReturnTrueFromInvalidFromSharingSameSidesOnBottom(self):
        
        cube = 'owgyrrrwowyrwgbyybgwwooryywrggybgoowbgyryrybogobgwobyr'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_unsolvableCubeDetection_970_ShouldReturnTrueFromInvalidFromSharingSameCubes(self):
        
        cube = 'wggbbgoowowgyrrrrowyrwgbyybgwwooryywyrogybbrybggbworob'
        
        expectedResult = True
        
        actualResult = unsolvableCubeDetection._unsolvableCubeDetection(cube)
        
        self.assertEqual(expectedResult, actualResult)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()