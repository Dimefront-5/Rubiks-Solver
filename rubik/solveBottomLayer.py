'''
Created on Sep 26, 2022

@author: Tyler Ray
'''

import rubik.validBottomLayer as validBottomLayer
import rubik.rotate as rotate
import rubik.triggerMoves as triggerMoves
import rubik.cubeConstants as constants
import rubik.creatingReturnDict as creatingReturnDict

def _solveBottomLayer(cube):
    rotations = ''
    outputDict = {}
    bottomMiddleCube = cube[constants.D11]
    
    isBottomLayer = validBottomLayer._validBottomLayer(cube)
    
    if isBottomLayer == True:
        outputDict = creatingReturnDict._creatingReturnDict(cube, rotations)
        return outputDict
    
    
    outputDict = _evaluateBottomLayer(cube, bottomMiddleCube)
    
    if outputDict == False:
        returnDict = {}
        returnDict['status'] = 'error: unsolvable cube'
        return returnDict
    
    return outputDict
 
 
def _evaluateBottomLayer(cube, bottomMiddleCube):
    rotations = ''
    #It has been very difficult to find a maximum loop reach for this cube due to the nature of how I wrote my code.
    #However I found that it mostly ends around 7 when I run a maximum. However I add two for unforeseen conditions
    maximumLoopReach = 9
    
    loopCount = 0
    while True:
        
        outputDict = _solveBottomFaceTopSidesCorners(cube, bottomMiddleCube)
        
        if outputDict == None:
            
            outputDict = _solveBottomFaceTopFaceCorners(cube, bottomMiddleCube)
            
            if outputDict == None:
                
                outputDict = _solveBottomFaceBottomCorners(cube, bottomMiddleCube)
                
                if outputDict == None:
                    
                    outputDict = _appearsToBeSolved(cube)
                    
        cube = outputDict['cube']
        rotations = rotations + outputDict['dir']
        
        
        isBottomSolved = validBottomLayer._validBottomLayer(cube)
        
        if isBottomSolved == True:
            returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
            return returnDict
        
        if loopCount > maximumLoopReach:
            return False
        
        loopCount = loopCount + 1


def _appearsToBeSolved(cube):
    index = constants.F20
    faceMiddleIndex = constants.F11
    distanceFromBottomLeftCubeToBottomRightCube = 2
    
    while index < len(cube):
        if cube[index] != cube[faceMiddleIndex]:
            outputDict = triggerMoves._triggerMoves(cube, index, 'Unsolved')
            return outputDict
        
        newIndex = _increaseIndexForBottom(index)
        if newIndex != index:
            index = newIndex
            faceMiddleIndex = index
            
        index = index + distanceFromBottomLeftCubeToBottomRightCube
      
def _solveBottomFaceBottomCorners(cube, bottomMiddleCube):
    index = constants.F20
    distanceFromBottomLeftCubeToBottomRightCube = 2
    
    while index < len(cube):
        if cube[index] == bottomMiddleCube:
            outputDict = triggerMoves._triggerMoves(cube, index, 'BottomCorner')
            return outputDict
        
        newIndex = _increaseIndexForBottom(index)
        if newIndex != index:
            index = newIndex
        index = index + distanceFromBottomLeftCubeToBottomRightCube
        
    return None


def _increaseIndexForBottom(index):
    pastLengthOfCube = 54
    
    if index == constants.F22:
        index = constants.R11
    elif index == constants.R22:
        index = constants.B11
    elif index == constants.B22:
        index = constants.L11
    elif index == constants.L22:
        index = pastLengthOfCube
    return index
    
def _solveForBttomFaceTopCornersWithoutCorners(cube, bottomMiddleCube):
    if cube[constants.U00] == bottomMiddleCube:
            outputDict = _findOppositeSide(cube, constants.D20, constants.U00)
            
    elif cube[constants.U02] == bottomMiddleCube:
            outputDict = _findOppositeSide(cube, constants.D22, constants.U02)
    
        
    elif cube[constants.U20] == bottomMiddleCube:
            outputDict = _findOppositeSide(cube, constants.D00, constants.U20)
    
    elif cube[constants.U22] == bottomMiddleCube:
            outputDict = _findOppositeSide(cube, constants.D02, constants.U22)
    else:    
        outputDict = None
    
    return outputDict

def _solveForCornersBeingOppositeWithTheSameColor(cube, bottomMiddleCube):
    rotations = ''
    if cube[constants.U00] == cube[constants.U22]:
        if cube[constants.U00] == bottomMiddleCube:
            outputDict = _findOppositeSide(cube, constants.D20, constants.U00)
            rotations = outputDict['dir']
        
        if cube[constants.U22] == bottomMiddleCube and (rotations == '' or rotations == 'U'):
            outputDict = _findOppositeSide(cube, constants.D02, constants.U22)
            
        if rotations == '':
            return None
        
    elif cube[constants.U02] == cube[constants.U20]:
        if cube[constants.U02] == bottomMiddleCube:
            outputDict = _findOppositeSide(cube, constants.D22, constants.U02)
            rotations = outputDict['dir']
            
        if cube[constants.U20] == bottomMiddleCube and (rotations == '' or rotations == 'U'):
            outputDict = _findOppositeSide(cube, constants.D00, constants.U20)            
        
        if rotations == '':
            return None
        
    else:
        return None
    
    return outputDict
    
def _solveBottomFaceTopFaceCorners(cube, bottomMiddleCube):
    
    if (cube[constants.U00] != cube[constants.U22]) and (cube[constants.U02] != cube[constants.U20]):
        outputDict = _solveForBttomFaceTopCornersWithoutCorners(cube, bottomMiddleCube)
        return outputDict
    
       
    outputDict = _solveForCornersBeingOppositeWithTheSameColor(cube, bottomMiddleCube)
    
    return outputDict
        
def _findOppositeSide(cube, opposingCornerIndex, cornerIndex):
    
    if cube[opposingCornerIndex] != cube[cornerIndex]:
        outputDict = triggerMoves._triggerMoves(cube, cornerIndex, 'Top')
        return outputDict
    else:
        outputDict = _rotateTopFace(cube)
        return outputDict
            
def _rotateTopFace(cube):
    inputDict = {}   
    inputDict['cube'] = cube
    inputDict['dir'] = 'U'
    outputDict = rotate._rotate(inputDict)
    inputDict['cube'] = outputDict['cube']
    
    return inputDict
  
def _solveBottomFaceTopSidesCorners(cube, bottomMiddleCube):
    cornerIndex = 0
    index = 0
    bottomMiddleIsFound = False
    modulusDivider = 2
    distanceFromTopLeftCubeToTopRightCube = 2
    
    while index < len(cube):
        if cube[index] == bottomMiddleCube:
            outputDict = _validateMiddleOpposing(index, cornerIndex, cube)
            bottomMiddleIsFound = True
            if outputDict['isMatch'] == True:
                return outputDict
        
        
        
        index = _increaseIndexForTop(index)
        cornerIndex = (cornerIndex + 1) % modulusDivider # We want to continue to keep the cornerIndex the same as index position. The modulus allows us to have two common numbers
        index = index + distanceFromTopLeftCubeToTopRightCube
        
        
    if bottomMiddleIsFound == True:
        outputDict = _rotateTopFace(cube)
        returnDict = _solveBottomFaceTopSidesCorners(outputDict['cube'], bottomMiddleCube)
        returnDict['dir'] = outputDict['dir'] + returnDict['dir']
        return returnDict
    
    return None            
            


def _increaseIndexForTop(index):
    pastLengthOfCube = 54
   
   
   
    if index == constants.F02: 
        newIndex = constants.F21
        
    elif index == constants.R02:
        newIndex  = constants.R21
        
    elif index == constants.B02:
        newIndex = constants.B21
        
    elif index == constants.L02:
        newIndex = pastLengthOfCube
        
    else:
        newIndex = index
    return newIndex          
            
def _validateMiddleOpposing(index, cornerIndex, cube):
    modulusDivider = 36
    distanceFromOppositeCorner = 7
    distanceFromRightCornerMiddle = 11
    distanceFromLeftCornerMiddle = 5
    topLeftCornerPosition = 0
    topRightCornerPosition = 1
    
    
    oppositeOfIndexTopLeftMiddleCube = (index - distanceFromLeftCornerMiddle) % modulusDivider
    oppositeOfIndexTopLeftCorner = (index - distanceFromOppositeCorner) % modulusDivider

    oppositeOfIndexTopRightCorner = (index + distanceFromOppositeCorner) % modulusDivider
    oppositeOfIndexTopRightMiddleCube = (index + distanceFromRightCornerMiddle) % modulusDivider
    
    outputDict = {}
    outputDict['isMatch'] = False    
    
    if cornerIndex == topLeftCornerPosition:
        if cube[oppositeOfIndexTopLeftCorner] == cube[oppositeOfIndexTopLeftMiddleCube]:
            outputDict = triggerMoves._triggerMoves(cube, oppositeOfIndexTopLeftCorner, 'TopCorner')
            outputDict['isMatch'] = True
            
    elif cornerIndex == topRightCornerPosition:
        if cube[oppositeOfIndexTopRightCorner] == cube[oppositeOfIndexTopRightMiddleCube]:
            outputDict = triggerMoves._triggerMoves(cube, oppositeOfIndexTopRightCorner, 'TopCorner')
            outputDict['isMatch'] = True
        
    return outputDict
