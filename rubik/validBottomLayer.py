'''
Created on Sep 26, 2022

@author: Tyler Ray
'''
import rubik.cubeConstants as constants

def _validBottomLayer(cube):
    isBottomValid = _validBottomFace(cube)
    
    if isBottomValid == False:
        return False
    
    isSidesValid = _validSides(cube)
    return isSidesValid



def _validBottomFace(cube):
    bottomMiddleCube = cube[constants.D11]
    
    for index in range(constants.D00, constants.lengthOfCube):
        if cube[index] != bottomMiddleCube:
            return False
        
    return True


def _validSides(cube):
    faceIndex = 1
        
    frontFaceMiddleCube = cube[constants.F11]
    
    rightfaceMiddleCube = cube[constants.R11]
    
    backfaceMiddleCube = cube[constants.B11]
    
    leftfaceMiddleCube = cube[constants.L11]
    
    index = constants.F20
    
    while index <= constants.L22:
                
        if faceIndex == 1:
            isMiddleEqual = _checkMiddleCube(cube, index, frontFaceMiddleCube)
        
        elif faceIndex == 2:
            isMiddleEqual = _checkMiddleCube(cube, index, rightfaceMiddleCube)    
            
        elif faceIndex == 3:
            isMiddleEqual = _checkMiddleCube(cube, index, backfaceMiddleCube)  
            
        elif faceIndex == 4:  
            isMiddleEqual = _checkMiddleCube(cube, index, leftfaceMiddleCube)
            
        if isMiddleEqual == False:
            return False
        
        newIndex = _increaseIndex(index)
        if newIndex != index:
            index = newIndex
            faceIndex = faceIndex + 1   
            
        index = index + 2
            
    return True        
            
def _checkMiddleCube(cube, index, middleFace):
    if cube[index] == middleFace:
        return True
    else:
        return False
    
    
    
def _increaseIndex(index):
    
    if index == constants.F22:
        return constants.R11
    elif index == constants.R22:
        return constants.B11
    elif index == constants.B22:
        return constants.L11
    elif index == constants.L22:
        return constants.lengthOfSideFacesCombined
    else:
        return index