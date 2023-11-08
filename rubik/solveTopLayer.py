'''
Created on Nov 5, 2022

@author: Tyler Ray
'''
import rubik.creatingReturnDict as creatingReturnDict
import rubik.validTopLayer as validTopLayer
import rubik.cubeConstants as constants
import rubik.rotateCommunicator as rotateCommunicator


distanceFromTopLeftToMiddle = 4
distanceFromTopLeftToTopMiddle = 1

def _solveTopLayer(cube):
    rotations = ''
    topLayerValidity = validTopLayer._validTopLayer(cube)
    if topLayerValidity != False:
        returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    else:
        returnDict = _solvingTheTopLayer(cube)
        
        if returnDict == False:
            returnDict = {}
            returnDict['status'] = 'error: unsolvable cube'
        
        
    return returnDict


#-----------Inward Facing Modules

def _solvingTheTopLayer(cube):
    rotations = ''
    
    loopCount = 0
    
    maximumLoopReach = 6
    
    while True:
        outputDict = _checkingForMatchingCorners(cube)
        
        if 'count' in outputDict:
            
            if outputDict['count'] == 1:
                outputDict = _oneMatchingCorner(cube)
                
            else:
                outputDict = _allMatchingCorners(cube)
            
        cube = outputDict['cube']
        rotations = rotations + outputDict['rotations']
        
        topValidity = validTopLayer._validTopLayer(cube)
        
        if topValidity == True:
            
            returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
            return returnDict
        
        if loopCount > maximumLoopReach:
            
            return False
        
        loopCount = loopCount + 1
            
    
    
    
def _rotateToSolveOneTopCornersMatchingFromNone(cube):
    rotations = 'lURuLUUrURUUr'
    
    rotatedCube = rotateCommunicator._rotateCommunicator(cube, rotations)
    
    returnDict = creatingReturnDict._creatingReturnDict(rotatedCube, rotations)
    
    return returnDict


def _checkingForMatchingCorners(cube):
    index = constants.F00
    distanceToNextTopCornerCube = 2
    matchingCornerCount = 0
    
    while index < constants.lengthOfSideFacesCombined:
        
        if cube[index] == cube[index + distanceToNextTopCornerCube]:
            matchingCornerCount = matchingCornerCount + 1
            
        index = index + constants.distanceToSameCubeOnNextFace
    
    if matchingCornerCount == 0:
        returnDict = _rotateToSolveOneTopCornersMatchingFromNone(cube)
        
    else:
        returnDict = {}
        returnDict['count'] = matchingCornerCount
        
    return returnDict
    
def _oneMatchingCorner(cube):
    index = constants.F00
    distanceToNextTopCornerCube = 2
    
    while index < constants.lengthOfSideFacesCombined:
        
        if cube[index] == cube[index + distanceToNextTopCornerCube]:
            outputDict = _determineRotation(cube, index)
            return outputDict
        
        index = index + constants.distanceToSameCubeOnNextFace
            
    
def _determineRotation(cube, index):
    outputDict = _lineUpMatch(cube, index)
    faceIndex = _determineFace(outputDict['index'])
    
    #We want the matching corners to be on our left side.
    if faceIndex == 'Front':
        rotations = 'fUBuFUUbUBUUb'
    elif faceIndex == 'Right':
        rotations = 'rULuRUUlULUUl'
    elif faceIndex == 'Back':
        rotations = 'bUFuBUUfUFUUf'
    else:
        rotations = 'lURuLUUrURUUr'
        
        
    cube = rotateCommunicator._rotateCommunicator(outputDict['cube'], rotations)
    
    rotations = outputDict['rotations'] + rotations
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    
    return returnDict

def _lineUpMatch(cube, index):
    distanceToMiddleCube = 4
    rotations = ''
    while True:
        
        if cube[index] == cube[index + distanceToMiddleCube]:
            returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
            returnDict['index'] = index
            return returnDict
        
        else:
            rotations = rotations + 'U'
            cube = rotateCommunicator._rotateCommunicator(cube, 'U')
            index = (index - constants.distanceToSameCubeOnNextFace) % constants.lengthOfSideFacesCombined
    
    
    
    
def _determineFace(index):   
    
    if index < constants.F22:
        return 'Front'
    elif index < constants.R22:
        return 'Right'
    elif index < constants.B22:
        return 'Back'
    else:
        return 'Left'





def _rotateToSolvedFace(cube, finishedTopFaceIndex):
    outputDict = _lineUpMatch(cube, finishedTopFaceIndex)
    
    cube = outputDict['cube']
    returnDict = _allMatchingCorners(cube)
    
    returnDict['rotations'] = outputDict['rotations'] + returnDict['rotations']
    
    return returnDict

def _allMatchingCorners(cube):
    index = constants.F00
    finishedTopFaceIndex = -1
        
    while index < constants.lengthOfSideFacesCombined:
        if cube[index] == cube[index + distanceFromTopLeftToTopMiddle]:
            
            finishedTopFaceIndex = index
            if cube[index] == cube[index + distanceFromTopLeftToMiddle]: 
                
                outputDict = _FlippingToFinish(cube, index)
                return outputDict
            
        index = index + constants.distanceToSameCubeOnNextFace
    
    
    
    if finishedTopFaceIndex != -1:
        returnDict = _rotateToSolvedFace(cube, finishedTopFaceIndex)
    
    else:#We need to do a counter rotation to get one finished up
        index = 0
        returnDict = _FlippingToFinish(cube, index)
    
    return returnDict
            
        

            
def _FlippingToFinish(cube, index):
    faceIndex = _determineFace(index)
    initialTurn = _determineIntialTurn(cube, index)
    
    if faceIndex == 'Front':
        rotations = _rotateSolvedFaceOnFront(initialTurn)
        
    elif faceIndex == 'Right':
        rotations = _rotateSolvedFaceOnRight(initialTurn)
        
    elif faceIndex == 'Back':
        rotations = _rotateSolvedFaceOnBack(initialTurn)
        
    else:
        rotations = _rotateSolvedFaceOnLeft(initialTurn)
    
    
    
    cube = rotateCommunicator._rotateCommunicator(cube, rotations)
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    
    return returnDict

def _rotateSolvedFaceOnFront(initialTurn):
    
    if initialTurn == 'Counter':
        rotations = 'BBuRlBBrLuBB'
        
    else:
        rotations = 'BBURlBBrLUBB'
    
    
    return rotations


def _rotateSolvedFaceOnRight(initialTurn):
    
    if initialTurn == 'Counter':
        rotations = 'LLufBLLFbuLL'
        
    else:
        rotations = 'LLUfBLLFbULL'
    
    
    return rotations

def _rotateSolvedFaceOnBack(initialTurn):
    
    if initialTurn == 'Counter':
        rotations = 'FFurLFFRluFF'
        
    else:
        rotations = 'FFUrLFFRlUFF'
    
    
    return rotations
        
    
def _rotateSolvedFaceOnLeft(initialTurn):
    
    if initialTurn == 'Counter':
        rotations = 'RRuFbRRfBuRR'
        
    else:
        rotations = 'RRUFbRRfBURR'
    
    
    return rotations


def _determineIntialTurn(cube, index):
    index = (index + constants.distanceToSameCubeOnNextFace) % constants.lengthOfSideFacesCombined
    
    distanceToMiddleCubeOnNextFace = constants.distanceToSameCubeOnNextFace + distanceFromTopLeftToMiddle
    
    cubeOnFaceToTheRight = (index + distanceToMiddleCubeOnNextFace) % constants.lengthOfSideFacesCombined
    
    topMiddleCubeIndex = index + distanceFromTopLeftToTopMiddle
    
    if cube[topMiddleCubeIndex] == cube[cubeOnFaceToTheRight]:
        return 'Counter'
    
    else:
        return 'Clockwise'
            
    
  
    