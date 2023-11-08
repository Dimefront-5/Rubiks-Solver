'''
Created on Sep 30, 2022

@author: Tyler Ray
'''

import rubik.cubeConstants as constants


def _validBottomCross(cube, bottomMiddleCube):
    outputDict = {}
    
    outputDict['crossPresence'] = False
    outputDict['daisyPresence'] = False
    crossPresence = _isCrossValid(cube, bottomMiddleCube)
    daisyPresence = _isDaisyValid(cube, bottomMiddleCube)
    
    if crossPresence == True:
        outputDict['crossPresence'] = True
    elif daisyPresence == True:
        outputDict['daisyPresence'] = True
    
    return outputDict
    
def _isSidesValid(cube):
    
    if cube[constants.F21] == cube[constants.F11] and cube[constants.R21] == cube[constants.R11]:
        
        if cube[constants.B21] == cube[constants.B11] and cube[constants.L21] == cube[constants.L11]:
            return True
            
    return False


def _isCrossValid(cube, bottomMiddleColor):
    
    if cube[constants.D01] == bottomMiddleColor and cube[constants.D12] == bottomMiddleColor :
        
        if cube[constants.D10] == bottomMiddleColor and cube[constants.D21] == bottomMiddleColor:
            
            isCubeComplete = _isSidesValid(cube)
            return isCubeComplete
          
    return False


def _isDaisyValid(cube, bottomMiddleColor):
    
    if cube[constants.U01] == bottomMiddleColor and cube[constants.U10] == bottomMiddleColor:
        
        if cube[constants.U12] == bottomMiddleColor and cube[constants.U21] == bottomMiddleColor:
            return True
        
    return False