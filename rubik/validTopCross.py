'''
Created on Oct 23, 2022

@author: Tyler Ray
'''

import rubik.cubeConstants as constants

def _validTopCross(cube):
    topMiddleCube = cube[constants.U11]
    
    crossValidity = _crossCheck(cube, topMiddleCube)
    
    return crossValidity



def _crossCheck(cube, topMiddleCube):
    index = constants.U01
    increment = 2
    
    while index < constants.U22:
        if cube[index] != topMiddleCube:
            return False
        
        index = index + increment
        
    return True