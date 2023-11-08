'''
Created on Oct 23, 2022

@author: Tyler Ray
'''

import rubik.cubeConstants as constants

def _validTopFace(cube):
    topMiddleCube = cube[constants.U11]
    
    isTopValid = _check(cube, topMiddleCube)
    
    return isTopValid
    
    
def _check(cube, topMiddleCube):
    index = constants.U00
    
    while index <= constants.U22:
        if cube[index] != topMiddleCube:
            return False
        index = index + 1
        
    return True