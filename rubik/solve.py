import rubik.solveBottomCross as solveBottomCross
import rubik.validation as validation
import rubik.solveBottomLayer as solveBottomLayer
import rubik.solveMiddleLayer as solveMiddleLayer
import rubik.redundancyReducer as redundancyReducer
import rubik.solveTopFace as solveTopFace
import rubik.integrityToken as integrityToken
import rubik.solveTopLayer as solveTopLayer
import rubik.unsolvableCubeDetection as unsolvableCubeDetection
import rubik.creatingReturnDict as creatingReturnDict
import rubik.validSolvedCube as validSolvedCube



'''
Created on Sep 12, 2022

@author: Tyler Ray
'''

def _solve(parms):
    #Return rotates needed to solve input cube
    
    initialCube = parms.get('cube',None)
    cubeValidity = _initialCubeCheck(initialCube)
    
    if cubeValidity != True:
        return cubeValidity
    
    
    outputDict = _solvingBottomFace(initialCube) 
    
    if 'status' in outputDict:
        return outputDict
    
    rotations = outputDict['rotations']
    
    outputDict = solveMiddleLayer._solveMiddleLayer(outputDict['cube'])
    
    if 'status' in outputDict:
        return outputDict
    
    cube = outputDict['cube']
    rotations = rotations + outputDict['rotations']
    
    outputDict = _solvingTopFaceAndLayer(cube, rotations)
    
    if 'status' in outputDict:
        return outputDict
    
    result = _createHashandReturnDictionary(initialCube, outputDict)
    
    return result


#------ Inward Facing Modules


def _initialCubeCheck(initialCube):
    result = {}
    
    cubeValidity = validation._validation(initialCube)
    
    if cubeValidity != 'ok' :
        result['status'] = cubeValidity
        return result
    
    unsolvableCube = unsolvableCubeDetection._unsolvableCubeDetection(initialCube)
    
    if unsolvableCube == True:
        result['status'] = 'error: unsolvable cube'
        return result
    
    return True


def _solvingBottomFace(cube):
    
    outputDict = solveBottomCross._solveBottomCross(cube)
    
    if outputDict == False:
        result = {}
        result['status'] = 'error: unsolvable cube'
        return result
        
    cube = outputDict['cube']
    rotations = outputDict['rotations']
    
    outputDict = solveBottomLayer._solveBottomLayer(cube)
    
    if 'status' in outputDict:
        return outputDict
    
    rotations = rotations + outputDict['rotations']  
    
    returnDict = creatingReturnDict._creatingReturnDict(outputDict['cube'], rotations)
    
    return returnDict

def _solvingTopFaceAndLayer(cube, rotations):
    
    outputDict = solveTopFace._solveTopFace(cube)
    
    if 'status' in outputDict:
        return outputDict
    
    rotations = rotations + outputDict['rotations']
    cube = outputDict['cube']
    
    outputDict = solveTopLayer._solveTopLayer(cube)
    
    result = {}
    result['rotations'] = rotations + outputDict['rotations']
    result['cube'] = outputDict['cube']
    return result



def _createHashandReturnDictionary(initialCube, outputDict):
    result = {}
    
    result['rotations'] = outputDict['rotations']

    result['rotations'] = redundancyReducer._redundancyReducer(result['rotations'])
    
    token = integrityToken._integrityToken(initialCube, result['rotations'])
    
    cubeValidity = validSolvedCube._validatingCube(outputDict['cube'])
    
    if cubeValidity == False: #If for some unforeseen reason, after everything if the cube is still unsolved, it is an unsolvable cube
        returnDict = {}
        returnDict['status'] = 'error: unsolvable cube'
        return returnDict
    
    
    result['status'] = 'ok'
    result['token'] = token
    
    return result
    
    
    
    