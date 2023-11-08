'''
Created on Oct 23, 2022

@author: Tyler Ray
'''

import rubik.validTopFace as validTopFace
import rubik.solveTopCross as solveTopCross
import rubik.cubeConstants as constants
import rubik.creatingReturnDict as creatingReturnDict
import rubik.rotateCommunicator as rotateCommunicator

def _solveTopFace(cube):
    outputDict = {}
    rotations = ''
    
    isTopValid = validTopFace._validTopFace(cube)
    
    if isTopValid == True:
        outputDict['rotations'] = rotations
        outputDict['cube'] = cube
    else:
        outputDict = solveTopCross._solveTopCross(cube)
        
        if 'status' in outputDict:
            return outputDict
        
        cube = outputDict['cube']
        rotations = outputDict['rotations']
        
        outputDict = _solvingTheTopFace(cube)
        
        if outputDict == False:
            returnDict = {}
            returnDict['status'] = 'error: unsolvable cube'
            return returnDict
        
        outputDict['rotations'] = rotations + outputDict['rotations']
    
    return outputDict


#--------Inward Facing Modules

def _solvingTheTopFace(cube):
    
    rotations = ''
    #My maximum for this loop should be 4, I added 2.
    
    loopCount = 0
    
    maximumLoopReach = 6
    while True:
        
        if loopCount > maximumLoopReach:
            return False
        
        outputDict = _findingFish(cube)
        
        if outputDict != None:
            cube = outputDict['cube']
            rotations = rotations + outputDict['rotations']
            
            faceValiditiy = validTopFace._validTopFace(cube)
            
            if faceValiditiy == True:
                returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
                return returnDict
                    
        else: 
            faceValiditiy = validTopFace._validTopFace(cube)
            
            if faceValiditiy == True:
                returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
                return returnDict
            outputDict = _positionCheck(cube)
            
            if outputDict == False:
                return False           
            cube = outputDict['cube']
            rotations = rotations + outputDict['rotations']
            
        loopCount = loopCount + 1
    
        


def _findingFish(cube):
    
    isFishPossible = _isFishPossible(cube)
    if isFishPossible == False:
        return None
    
    
    isFishValid = _isFishValid(cube)
    
    if isFishValid == True:
        outputDict = _rotationCombination(cube)
        return outputDict
    
    outputDict = _rotatingToFish(cube)
    
    cube = outputDict['cube']
    rotations = outputDict['rotations']
    
    
    outputDict = _rotationCombination(cube)
    
    rotations = rotations + outputDict['rotations']
    cube = outputDict['cube']
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    
    return returnDict

def _rotatingToFish(cube):
    rotations = ''
    while True:
        
        cube = rotateCommunicator._rotateCommunicator(cube, 'U')
        rotations = rotations + 'U'
        
        fishValidity = _isFishValid(cube)
        
        if fishValidity == True:
            
            returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
            return returnDict
            
    
def _isFishPossible(cube):
    index = constants.U00
    fishPossibilityCount = 0
    
    finalIndex = constants.U22
    
    while index <= finalIndex:
        if cube[index] == cube[constants.U11]:
            fishPossibilityCount = fishPossibilityCount + 1
        
        if index == constants.U02:
            index = constants.U20
            
        else:   
            index = index + 2
        
    
    if fishPossibilityCount == 1:
        return True
    
    return False      
    
def _isFishValid(cube):
    index = constants.U01
    
    emptyPartOfFish = constants.U02
    
    while index < constants.U22:
        
        if index != emptyPartOfFish:
            
            if cube[index] != cube[constants.U11]:
                
                return False
            
        index = index + 1
        
    return True
    
def _positionCheck(cube):
    #Maximum Loop Count for this loop is 3
    
    loopCount = 0
    
    maximumLoopReach = 3
    
    rotations = ''
    while cube[constants.U11] != cube[constants.L02]:
        cube = rotateCommunicator._rotateCommunicator(cube, 'U')
        rotations = rotations + 'U'
        
        if loopCount > maximumLoopReach:
            return False
        
        loopCount = loopCount + 1
    
    outputDict = _rotationCombination(cube)
    outputDict['rotations'] = rotations + outputDict['rotations']
    
    return outputDict


def _rotationCombination(cube):
    rotations = 'RUrURUUr'
    
    cube = rotateCommunicator._rotateCommunicator(cube, rotations)
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    
    return returnDict
    
    
    
