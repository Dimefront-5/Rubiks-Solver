'''
Created on Sep 29, 2022

@author: Tyler Ray
'''
import rubik.rotate as rotate
import rubik.cubeConstants as constants

def _triggerMoves(cube, index, identification):
    
    if identification == 'TopCorner':
        outputDict = _topCornerTrigger(cube, index)
        
    elif identification == 'BottomCorner':
        outputDict = _bottomCornerTrigger(cube, index)
    elif identification == 'Top':
        outputDict = _topTrigger(cube, index)
        
    elif identification == 'Unsolved':
        outputDict = _unsolvedTrigger(cube, index)
        
    return outputDict
    
    
def _determineLeftRotation(cube, index):
        
    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.L00:
        rotations = 'buB'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    elif index == constants.L02:
        rotations = 'FUf'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
    
    
    inputDict['cube'] = outputDict['cube']
    return inputDict
        
def _determineBackRotation(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.B00:
        rotations = 'ruR'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
    elif index == constants.B02:
        rotations = 'LUl'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
        
    inputDict['cube'] = outputDict['cube']
    return inputDict    
        
def _determineRightRotation(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.R00:
        rotations = 'fuF'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
    elif index == constants.R02:
        rotations = 'BUb'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
    
    
    inputDict['cube'] = outputDict['cube']
    return inputDict 

def _determineFrontRotation(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.F00:
        rotations = 'luL'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    elif index == constants.F02:
        rotations = 'RUr'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    inputDict['cube'] = outputDict['cube']
    return inputDict 
    
def _topCornerTrigger(cube, index):
    
    faceIndex = _determineFace(index)
    if faceIndex == 'front':
        outputDict = _determineFrontRotation(cube, index)
    elif faceIndex == 'right':
        outputDict = _determineRightRotation(cube, index)
    elif faceIndex == 'back':
        outputDict = _determineBackRotation(cube, index)
    elif faceIndex == 'left':
        outputDict = _determineLeftRotation(cube, index)
        
    return outputDict

    
def _bottomCornerTrigger(cube, index):
    faceIndex = _determineFace(index)
    
    if faceIndex == 'front':
        outputDict = _triggerFromBottomFront(cube, index)
    elif faceIndex == 'right':
        outputDict = _triggerFromBottomRight(cube, index)
    elif faceIndex == 'back':
        outputDict = _triggerFromBottomBack(cube, index)
    elif faceIndex == 'left':
        outputDict = _triggerFromBottomLeft(cube, index)
        
    return outputDict


def _triggerFromBottomLeft(cube, index):
    
    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.L20:
        rotations = 'bUB'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    elif index == constants.L22: 
        rotations = 'Fuf'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    inputDict['cube'] = outputDict['cube']
    return inputDict

def _triggerFromBottomBack(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.B20:
        rotations = 'rUR'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    elif index == constants.B22: 
        rotations = 'Lul'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    inputDict['cube'] = outputDict['cube']
    return inputDict

def _triggerFromBottomRight(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.R20:
        rotations = 'fUF'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    elif index == constants.R22: 
        rotations = 'Bub'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    inputDict['cube'] = outputDict['cube']
    return inputDict

def _triggerFromBottomFront(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    
    if index == constants.F20:
        rotations = 'lUL'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    elif index == constants.F22: 
        rotations = 'Rur'
        inputDict['dir'] = rotations
        outputDict = rotate._rotate(inputDict)
        
    inputDict['cube'] = outputDict['cube']
    return inputDict

    
def _topTrigger(cube, index):

    inputDict = {}
    inputDict['cube'] = cube
    if index == constants.U00:
        outputDict = _rotateTopLeftCornerToDown(inputDict)
    elif index == constants.U02:
        outputDict = _rotateTopRightCornerToDown(inputDict)   
    elif index == constants.U20:
        outputDict = _rotateBottomLeftCornerToDown(inputDict)
    elif index == constants.U22:
        outputDict = _rotateBottomRightCornerToDown(inputDict)
    
    return outputDict

def _rotateTopLeftCornerToDown(inputDict):
    rotations = 'Lul'
    inputDict['dir'] = rotations
    outputDict = rotate._rotate(inputDict)
    inputDict['cube'] = outputDict['cube']
    return inputDict

def _rotateTopRightCornerToDown(inputDict):
    rotations = 'rUR'
    inputDict['dir'] = rotations
    outputDict = rotate._rotate(inputDict)
    inputDict['cube'] = outputDict['cube']
    return inputDict

def _rotateBottomLeftCornerToDown(inputDict):
    rotations = 'lUL'
    inputDict['dir'] = rotations
    outputDict = rotate._rotate(inputDict)
    inputDict['cube'] = outputDict['cube']
    return inputDict

def _rotateBottomRightCornerToDown(inputDict):
    rotations = 'Rur'
    inputDict['dir'] = rotations
    outputDict = rotate._rotate(inputDict)
    inputDict['cube'] = outputDict['cube']
    return inputDict


def _unsolvedTrigger(cube, index):
    
    faceIndex = _determineFace(index)
    if faceIndex == 'front':
        outputDict = _triggerFromBottomFront(cube, index)
    elif faceIndex == 'right':
        outputDict = _triggerFromBottomRight(cube, index)
    elif faceIndex == 'back':
        outputDict = _triggerFromBottomBack(cube, index)
    elif faceIndex == 'left':
        outputDict = _triggerFromBottomLeft(cube, index)
        
    return outputDict
    
    
def _determineFace(index):
    endOfFrontFace = 9
    endOfRightFace = 17
    endOfBackFace = 26
    endOfLeftFace = 35
    
    if index < endOfFrontFace:
        faceIndex = 'front'
    elif index >= endOfFrontFace and index <= endOfRightFace:
        faceIndex = 'right'
    elif index > endOfRightFace and index <= endOfBackFace:
        faceIndex = 'back'
    elif index > endOfBackFace and index <= endOfLeftFace:
        faceIndex = 'left'
        
    return faceIndex