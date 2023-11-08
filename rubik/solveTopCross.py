'''
Created on Oct 23, 2022

@author: Tyler Ray
'''
import rubik.validTopCross as validTopCross
import rubik.cubeConstants as constants
import rubik.creatingReturnDict as creatingReturnDict
import rubik.rotateCommunicator as rotateCommunicator

def _solveTopCross(cube):

    crossValiditiy = validTopCross._validTopCross(cube)
    
    if crossValiditiy == True:
        rotations = ''
        returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
        
    else:
        returnDict = _solvingTopCross(cube)
        
        if returnDict == False:
            returnDict = {}
            returnDict['status'] = 'error: unsolvable cube'
            
    return returnDict

#--------Inward Facing Modules

def _solvingTopCross(cube):
    rotations = ''
    #From my tests, the maximum it should take to loop through this should be 3, I added two.
    
    loopCount = 0
    
    maximumLoopReach = 5
    while True:
        outputDict = _lineTurn(cube)
        
        cube = outputDict['cube']
        rotations = rotations + outputDict['rotations']
        
        outputDict = _lTurn(cube)
        
        cube = outputDict['cube']
        rotations = rotations + outputDict['rotations']
        
        crossValidity = validTopCross._validTopCross(cube)
        
        if crossValidity == True:
            returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
            return returnDict
        
        elif loopCount > maximumLoopReach:
            return False
        else:
            outputDict = _rotateFromNoLorLine(cube)
            cube = outputDict['cube']
            rotations = rotations + outputDict['rotations']
            
        loopCount = loopCount + 1
            
            

def _rotateFromNoLorLine(cube):
    rotations = 'FURurf'
    cube = rotateCommunicator._rotateCommunicator(cube, rotations)
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    
    return returnDict

def _lTurn(cube):
    
    lValidity = _lCheck(cube)
    rotations = ''
    
    if lValidity == True:
        
        while True:
            
            if cube[constants.U01] == cube[constants.U11] and cube[constants.U10] == cube[constants.U11]:
                
                rotations = rotations + 'FURurf'
                cube = rotateCommunicator._rotateCommunicator(cube, 'FURurf')
                
                break
            
            rotations = rotations + 'U'
            cube = rotateCommunicator._rotateCommunicator(cube, 'U')
    
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    return returnDict
                


def _lCheck(cube):
    
    if cube[constants.U01] == cube[constants.U11]: 
        
        if cube[constants.U12] == cube[constants.U11] or cube[constants.U10] == cube[constants.U11]:
            return True
        
    if cube[constants.U21] == cube[constants.U11]:
        
        if cube[constants.U10] == cube[constants.U11] or cube[constants.U12] == cube[constants.U11]:
            return True
        
        
    return False
    
def _lineTurn(cube):
    lineValidity = _lineCheck(cube)
    rotations = ''
    
    if lineValidity == 'Vertical':
        rotations = 'FURurf'
        cube = rotateCommunicator._rotateCommunicator(cube, rotations)
    elif lineValidity == 'Horizontal':
        rotations = 'UFURurf'
        cube = rotateCommunicator._rotateCommunicator(cube, rotations)
    
    
    returnDict = creatingReturnDict._creatingReturnDict(cube, rotations)
    return returnDict
        
        
        
        
def _lineCheck(cube):
    
    if cube[constants.U01] == cube[constants.U11] and cube[constants.U21] == cube[constants.U11]:
        return 'Vertical'
    
    elif cube[constants.U10] == cube[constants.U11] and cube[constants.U12] == cube[constants.U11]:
        return 'Horizontal'
    
    return 'None'
