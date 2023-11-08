'''
Created on Oct 10, 2022

@author: Tyler Ray
'''
import rubik.cubeConstants as constants

def _validMiddleLayer(cube):
    isMiddleValid = _validColors(cube)
    return isMiddleValid


def _validColors(cube):
    index = 3
    middleIndex = constants.F11
    distanceFromSideCubes = 2
    
    while index < len(cube):
        if cube[index] != cube[middleIndex]:
            return False
        newIndex = _increaseIndexToNextFace(index)
        if newIndex != index:
            middleIndex = middleIndex + constants.distanceToSameCubeOnNextFace
            index = newIndex
        index = index + distanceFromSideCubes
    
    return True
    
def _increaseIndexToNextFace(index):

   
    if index == constants.F12:
        index = constants.R01
    elif index == constants.R12:
        index = constants.B01
    elif index == constants.B12:
        index = constants.L01
    elif index == constants.L12:
        index = constants.lengthOfCube
    return index