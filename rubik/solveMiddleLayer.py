'''
Created on Oct 10, 2022

@author: Tyler Ray
'''

import rubik.validMiddleLayer as validMiddleLayer
import rubik.rotateAway as rotateAway
import rubik.rotate as rotate
import rubik.triggerMoves as triggerMoves
import rubik.cubeConstants as constants
import rubik.creatingReturnDict as creatingReturnDict

def _solveMiddleLayer(cube):
    
    outputDict = {}
    isMiddleValid = validMiddleLayer._validMiddleLayer(cube) 
    
    if isMiddleValid == True:
        outputDict['cube'] = cube
        outputDict['rotations'] = ''
    else: 
        outputDict = _solveMiddle(cube)
        
        if outputDict == False:
            returnDict = {}
            returnDict['status'] = 'error: unsolvable cube'
            return returnDict
        
    return outputDict


def _solveMiddle(cube):
    rotations = ''
    #From my tests 6 seems to be the maximum amount of loops it will take to solve the middle layer, added 2 for unforeseen circumstances
    
    loopCount = 0
    maximumLoopReach = 8
    
    while True:
        outputDict = _findTopMiddleWithNoTopColors(cube)
        
        if outputDict == None:
            outputDict = _findMiddleSidePieces(cube)
        
        
        cube = outputDict['cube']
        rotations = rotations + outputDict['rotations']
        
        isMiddleValid = validMiddleLayer._validMiddleLayer(cube)
        if isMiddleValid == True:
            returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
            
            return returnDict
        
        loopCount = loopCount + 1
        
        if loopCount > maximumLoopReach:
            return False
        
        
def _findTopMiddleWithNoTopColors(cube):
    topMiddleCube = cube[constants.U11]
    index = 1 
    finalTopSideIndex = constants.L01
    
    while index <= finalTopSideIndex:
        
        if cube[index] != topMiddleCube:
            
            isTopMiddleColor = _checkTopIndex(cube, index, topMiddleCube)
            
            if isTopMiddleColor != True:
                
                outputDict = _lineUpWithMiddleFaceColor(cube, index)
                return outputDict
                
        index = index + constants.distanceToSameCubeOnNextFace
        
    return None
            
            
def _checkTopIndex(cube, index, topMiddleCube):
    topIndex = 0
    
    if index == constants.F01:
        topIndex = constants.U21
        
    elif index == constants.R01:
        topIndex = constants.U12
        
    elif index == constants.B01:
        topIndex = constants.U01
        
    elif index == constants.L01:
        topIndex = constants.U10
    
    if cube[topIndex] == topMiddleCube:
        return True
    
    return False
        
def _lineUpWithMiddleFaceColor(cube, index):
    inputDict = {}
    inputDict['cube'] = cube
    distancetoMiddleCube = 3
    middleCubeIndex = index + distancetoMiddleCube
    
    if cube[index] == cube[middleCubeIndex]:
        outputDict = rotateAway._rotateAway(cube, index)
        return outputDict
    
    else:
        outputDict = _rotateToLineUp(inputDict, index)
        return outputDict
        
        

def _rotateToLineUp(inputDict, index):    

    inputDict['dir'] = 'U'
    outputDict = rotate._rotate(inputDict)
    
    index = (index - constants.distanceToSameCubeOnNextFace) % constants.lengthOfSideFacesCombined
    
    outputDict = _lineUpWithMiddleFaceColor(outputDict['cube'], index)
    
    
    rotations = inputDict['dir'] + outputDict['rotations']
    returnDict = creatingReturnDict._creatingReturnDict(outputDict['cube'], rotations)
    
    return returnDict
        
        
def _findMiddleSidePieces(cube):       
    middleCubeIndex = constants.F11
    index = constants.F10
    distanceBetweenSides = 2
    
    while index < constants.lengthOfCube:
        if cube[index] != cube[middleCubeIndex]:
            outputDict = _determineTriggerMoveForSideLocations(cube, index)
            return outputDict
        
        newIndex = _increaseSideIndex(index)
        if newIndex != index:
            middleCubeIndex = middleCubeIndex + constants.distanceToSameCubeOnNextFace
            index = newIndex
        index = index + distanceBetweenSides
        
    return None
        
def _determineTriggerMoveForSideLocations(cube, index):
    inputDict = {}
    distanceFromSideToAboveCorner = 3
    indexOfTopRotation = 1
    
    cornerIndex = index - distanceFromSideToAboveCorner
    
    outputDict = triggerMoves._triggerMoves(cube, cornerIndex, 'TopCorner')
    rotations = outputDict['dir']
    
    inputDict['dir'] = outputDict['dir'][indexOfTopRotation].swapcase() #We want to rotate top back for white to be lined back up to turn it back down. We just do it the opposite of the trigger move top rotation
    inputDict['cube'] = outputDict['cube']
    outputDict = rotate._rotate(inputDict)
    
    cube = outputDict['cube']
    rotations = rotations + inputDict['dir']
    
    oppositeIndex = _determineOppositeSide(index)
    oppositeIndexCorner = oppositeIndex - distanceFromSideToAboveCorner
    
    outputDict = triggerMoves._triggerMoves(cube, oppositeIndexCorner, 'TopCorner')
    
    rotations = rotations + outputDict['dir']
    returnDict = creatingReturnDict._creatingReturnDict(outputDict['cube'], rotations)
    
    return returnDict
    

def _determineOppositeSide(index):
    
    distanceToOtherSideOfCube = 7
    
    rightIndex = (index + distanceToOtherSideOfCube) % constants.lengthOfSideFacesCombined
    leftIndex = (index - distanceToOtherSideOfCube) % constants.lengthOfSideFacesCombined
    
    #The only valid indicies for the a opposite side of a cube on the right side of the face are these
    frontLeftSideIndex = constants.F10
    rightLeftSideIndex = constants.R10
    backLeftSideIndex = constants.B10
    leftLeftSideIndex = constants.L10
    
    #If it is none of these, we know the cube is on the left side of the face
    if rightIndex == frontLeftSideIndex or rightIndex == rightLeftSideIndex:
        return rightIndex
    elif rightIndex == backLeftSideIndex or rightIndex == leftLeftSideIndex:
        return rightIndex
    else:
        return leftIndex
        
    
def _increaseSideIndex(index):       
        
    if index == constants.F12:
        index = constants.R01
        
    elif index == constants.R12:
        index = constants.B01
        
    elif index == constants.B12:
        index = constants.L01
        
    elif index == constants.L12:
        index = constants.lengthOfCube
        
    return index
        
        
        
        
        