'''
Created on Nov 9, 2022

@author: Tyler Ray
'''
import rubik.cubeConstants as constants

def _validSolvedCube(cube):
    solvedValidity = _validatingCube(cube)

    return solvedValidity



def _validatingCube(cube):
    index = constants.F00
    middleCube = constants.F11
    lengthOfAFace = 9
    
    while index < constants.lengthOfCube:
        if cube[index] != cube[middleCube]:
            return False
        
        else:
            index = index + 1
            
            if index % lengthOfAFace == 0:
                middleCube = middleCube + constants.distanceToSameCubeOnNextFace
    
    return True
        
    