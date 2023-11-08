'''
Created on Nov 5, 2022

@author: Tyler
'''
import rubik.cubeConstants as constants

def _validTopLayer(cube):
    topLayerValidity = _determingIfTopLayerisMatching(cube)
    return topLayerValidity
    
    
#----------- Inward Facing Modules


def _determingIfTopLayerisMatching(cube):
    index = constants.F00
    middleFaceCubeIndex = constants.F11

    while index < constants.lengthOfSideFacesCombined:
        if cube[index] != cube[middleFaceCubeIndex]:
            return False
        
        else:
            newIndex = _indexIncreaser(index)
            
            if newIndex != index:
                index = newIndex
                middleFaceCubeIndex = middleFaceCubeIndex + constants.distanceToSameCubeOnNextFace
                
            else:
                index = index + 1
                
    return True


def _indexIncreaser(index):
    
    if index == constants.F02:
        index = constants.R00
        
    elif index == constants.R02:
        index = constants.B00
        
    elif index == constants.B02:
        index = constants.L00
        
    elif index == constants.L02:
        index = constants.lengthOfCube
        
    return index
