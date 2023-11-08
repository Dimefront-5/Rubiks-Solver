'''
Created on Oct 10, 2022

@author: Tyler Ray
'''
import rubik.rotate as rotate
import rubik.triggerMoves as triggerMoves
import rubik.cubeConstants as constants

def _rotateAway(cube, index):
    outputDict = _determineTopRotation(cube, index)
    
    return outputDict


def _determineTopIndex(index):
    
    topIndex = 0
    if index == constants.F01:
        topIndex = constants.U21
    elif index == constants.R01:
        topIndex = constants.U12
    elif index == constants.B01:
        topIndex = constants.U01
    elif index == constants.L01:
        topIndex = constants.U10
        
    return topIndex
    
    
def _determineTopRotation(cube, index):
    distanceFromMiddleIndexToMiddleCubeOnRightAdjacentFace = 12
    distanceFromMiddleIndexToMiddleCubeOnleftAdjacentFace = 6
            
    rightSideMiddleIndex = (index + distanceFromMiddleIndexToMiddleCubeOnRightAdjacentFace) % constants.lengthOfSideFacesCombined
    leftSideMiddleIndex = (index - distanceFromMiddleIndexToMiddleCubeOnleftAdjacentFace) % constants.lengthOfSideFacesCombined
    
    topIndex = _determineTopIndex(index)
    
    inputDict = {}
    inputDict['cube'] = cube
    if cube[topIndex] == cube[rightSideMiddleIndex]:
        inputDict['dir'] = 'U'
        outputDict = _rotateLeftRotation(inputDict, index)
        
    elif cube[topIndex] == cube[leftSideMiddleIndex]:
        inputDict['dir'] = 'u'
        outputDict = _rotateRightRotation(inputDict, index)
        
    return outputDict
        



def _rotateLeftRotation(inputDict, index):
    distancetoOppositeSide = 7
    
    rightCornerIndex = index + 1
    
    
    otherSideOfCube = (rightCornerIndex + distancetoOppositeSide) % constants.lengthOfSideFacesCombined
    
    returnDict = _rotateTopToSide(inputDict, otherSideOfCube, rightCornerIndex)
  
    return returnDict


def _rotateRightRotation(inputDict, index):
    distancetoOppositeSide = 7

    leftCornerIndex = index - 1
    
    otherSideOfCube = (leftCornerIndex - distancetoOppositeSide) % constants.lengthOfSideFacesCombined
    
    returnDict = _rotateTopToSide(inputDict, otherSideOfCube, leftCornerIndex)
    

    return returnDict


def _rotateTopToSide(inputDict, otherSideOfCube, cornerIndex):
    
    outputDict = _rotateTop(inputDict)
    rotations = inputDict['dir']
        
    outputDict = triggerMoves._triggerMoves(outputDict['cube'], cornerIndex, 'TopCorner')
        
    rotations = rotations + outputDict['dir']
    
    inputDict['cube'] = outputDict['cube']
    outputDict = _rotateBackToOriginal(inputDict)
    rotations = rotations + outputDict['dir']
        
    outputDict = triggerMoves._triggerMoves(outputDict['cube'], otherSideOfCube , 'TopCorner')
    
    rotations = rotations + outputDict['dir']
    
    returnDict = {}
    
    returnDict['cube'] = outputDict['cube']
    returnDict['rotations'] = rotations

    return returnDict
    
def _rotateTop(inputDict):
    
    returnDict = {}
    
    outputDict = rotate._rotate(inputDict)
    
    returnDict['cube'] = outputDict['cube']
    returnDict['rotations'] = inputDict['dir']
    
    return returnDict

def _rotateBackToOriginal(inputDict):
    
    inputDict['dir'] = inputDict['dir'].swapcase()
    
    outputDict = _rotateTop(inputDict)
    
    outputDict['dir'] = inputDict['dir']
    
    return outputDict
    