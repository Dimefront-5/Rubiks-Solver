'''
Created on Sep 12, 2022

@author: Tyler Ray
'''

import rubik.rotate as rotate
import rubik.validBottomCross as validBottomCross
import rubik.cubeConstants as constants
import rubik.creatingReturnDict as creatingReturnDict


def _solveBottomCross(cube):
    
    outputDict = {}
    directions = ''
    bottomMiddleColor = cube[constants.D11]
    
    presenceOutput = validBottomCross._validBottomCross(cube, bottomMiddleColor)
    
    if presenceOutput['crossPresence'] == True:
        outputDict['rotations'] = directions
        outputDict['status'] = 'ok'
        outputDict['cube'] = cube
        return outputDict
    
    if presenceOutput['daisyPresence'] == True:
        outputDict = _solvingtheCross(cube, directions, bottomMiddleColor)
        
        cube = outputDict['cube']
        directions = outputDict['dir']
        
    else: 
        
        outputDict = _solvingTheDaisy(cube, directions, bottomMiddleColor)
        
        
        if outputDict != False:
            
            cube = outputDict['cube']
            directions = outputDict['dir']


            outputDict = _solvingtheCross(cube, directions, bottomMiddleColor)
            
            if outputDict != False:
                cube = outputDict['cube']
                directions = outputDict['dir']
            else:
                return False
            
        else:
            return False
    
        
    finaloutputDict = creatingReturnDict._creatingReturnDict(cube, directions)
    finaloutputDict['status'] = 'ok'
    return finaloutputDict

# ------------- Inward Facing Modules


def _solvingTheDaisy(cube, directions, bottomMiddleColor):
    #Since my algorithm makes sure not to displace already placed cubes, this loop's maximum is 7. I thought it was 4, but I was incorrect.
    maximumLoopReach = 7
    
    loopCount = 0
    while True:
        
        outputDict = _createDaisy(cube, directions, bottomMiddleColor)
        
        cube = outputDict['cube']
        directions = outputDict['dir']
        
        outputPresence = validBottomCross._validBottomCross(cube, bottomMiddleColor)
        
        if outputPresence['daisyPresence'] == True:
                    
                    return outputDict
                
        loopCount = loopCount + 1
        
        if loopCount > maximumLoopReach:
            return False

                    
def _solvingtheCross(cube, directions, bottomMiddleColor):
    flipCount = 0
    #My algorithm will rotate the top and return a 'U' There can be a maximum of 3 top turns and 4 Side turns.
    #It should only take at MOST 7 rotations to find all flips.
    
    maximumLoopReach = 7
    loopCount = 0
    
    while True:
        
        outputDict = _flipDaisy(cube, bottomMiddleColor)
        
        cube = outputDict['cube']
        directions = directions + outputDict['dir']
        flipCount = flipCount + outputDict['flip']
        
        if flipCount == 4 :
            
            outputDict['dir'] = directions
            outputDict['flip'] = flipCount
            
            return outputDict
        
        loopCount = loopCount + 1
        
        if loopCount > maximumLoopReach:
            return False
        
        
        
        

# ------------ Rotating/validating the cube
def _move(inputDict, topIndex, index):
    directions = ''
    cube = inputDict['cube']
    color = cube[index]
    
    #This solves an odd corner case that can cause infinite loops. Rotates the face before you rotate top.
    if len(inputDict['dir']) == 2 and inputDict['dir'][0] != inputDict['dir'][1]:
        directions = inputDict['dir'][0]
        inputDict = _rotatebeforeCollision(inputDict)
        
        
    topRotations = _collisionDetection(inputDict['cube'], topIndex, color)
    
    directions = directions + topRotations + inputDict['dir']
    
    inputDict['dir'] = topRotations + inputDict['dir']
    
    outputDict = rotate._rotate(inputDict)
    
    outputDict['dir'] = directions
    
    return outputDict


def _rotatebeforeCollision(inputDict):
    outputDict = {}
    outputDict['dir'] = inputDict['dir'][1]
    inputDict['dir'] = inputDict['dir'][0]
    inputDict = rotate._rotate(inputDict)
    outputDict['cube'] = inputDict['cube']
    return outputDict


def _collisionDetection(cube, topIndex, color):
    directions = ''
    outputDict = {}
    
    while True:
        
        if color == cube[topIndex]:
            
            outputDict = _rotateTopOfDaisy(cube)
            directions = directions + 'U'
            cube = outputDict['cube']
            
        else:
            return directions

            
def _determineLocation(locationIndicator):

    if locationIndicator % 5 == 0:
        return "top"
    
    elif locationIndicator % 5 == 1:
        return "left"
    
    elif locationIndicator % 5 == 2:
        return "right"
    
    elif locationIndicator % 5 == 3:
        return "bottom"   
 
            
def _rotateBottomFace(inputDict, index, location):
    
    if location == "top":
        inputDict['dir'] = 'FF'
        outputDict = _move(inputDict, constants.U21, index)
        return outputDict
            
    elif location == "left":
        inputDict['dir'] = 'LL'
        outputDict = _move(inputDict, constants.U10, index)
        return outputDict

    elif location == "right":
        inputDict['dir'] = 'RR'
        outputDict = _move(inputDict, constants.U12, index)
        return outputDict

    elif location == "bottom":      
        inputDict['dir'] = 'BB'
        outputDict = _move(inputDict, constants.U01, index)
        return outputDict    


def _rotateLeftFace(inputDict, index, location):
    
    if location == "top":
        inputDict['dir'] = 'LF'
        outputDict = _move(inputDict, constants.U21, index)
        return outputDict
            
    elif location == "left":
        inputDict['dir'] = 'b'
        outputDict = _move(inputDict, constants.U01, index)
        return outputDict

    elif location == "right":
        inputDict['dir'] = 'F'
        outputDict = _move(inputDict, constants.U21, index)
        return outputDict

    elif location == "bottom":
        inputDict['dir'] = 'Lb'
        outputDict = _move(inputDict, constants.U10, index)
        return outputDict

            
def _rotateBackFace(inputDict, index, location):
    
    if location == "top":
        inputDict['dir'] = 'BL'
        outputDict = _move(inputDict, constants.U10, index)
        return outputDict
            
    elif location == "left":
        inputDict['dir'] = 'r'
        outputDict = _move(inputDict, constants.U12, index)
        return outputDict

    elif location == "right":       
        inputDict['dir'] = 'L'
        outputDict = _move(inputDict, constants.U10, index)
        return outputDict

    elif location == "bottom":
        inputDict['dir'] = 'Br'
        outputDict = _move(inputDict, constants.U12, index)
        return outputDict        

            
def _rotateRightFace(inputDict, index, location):
    
    if location == "top":
        inputDict['dir'] = 'RB'
        outputDict = _move(inputDict, constants.U01, index)
        return outputDict
    
    elif location == "left":
        inputDict['dir'] = 'f'
        outputDict = _move(inputDict, constants.U21, index)
        return outputDict

    elif location == "right":
        inputDict['dir'] = 'B'
        outputDict = _move(inputDict, constants.U01, index)
        return outputDict

    elif location == "bottom":    
        inputDict['dir'] = 'Rf'
        outputDict = _move(inputDict, constants.U21, index)
        return outputDict

            
def _rotateFrontFace(inputDict, index, location):
    
    if location == "top":
        inputDict['dir'] = 'FR'
        outputDict = _move(inputDict, constants.U12, index)
        return outputDict
            
    elif location == "left":
        inputDict['dir'] = 'l'
        outputDict = _move(inputDict, constants.U10, index)
        return outputDict

    elif location == "right":
        inputDict['dir'] = 'R'
        outputDict = _move(inputDict, constants.U12, index)
        return outputDict

    elif location == "bottom":
        inputDict['dir'] = 'Fl'
        outputDict = _move(inputDict, constants.U10, index)
        return outputDict


def _faceCollisionDetection(cube, index, topIndex, location):
    outputDict = {}
    directions = ''
    while True:
        if cube[index] == cube[topIndex]:
            if location == 'top' or location == 'bottom':
                outputDict = _rotateTopOfDaisy(cube)
                directions = directions + outputDict['dir']
        else:
            outputDict['dir'] = directions
            return outputDict


def _rotatetoDaisy(cube, index, locationIndicator):
  
  
    faceIndex = _determineFaceIndex(cube, index)
    inputDict = {}
    inputDict['cube'] = cube
    location = _determineLocation(locationIndicator)
    
    match faceIndex:
        case 1:
            
            outputDict = _rotateFrontFace(inputDict, index, location)
            return outputDict
            
        case 2:
            outputDict = _rotateRightFace(inputDict, index, location)
            return outputDict
        case 3:
            outputDict = _rotateBackFace(inputDict, index, location)
            return outputDict
            
        case 4:
            outputDict = _rotateLeftFace(inputDict, index, location)
            return outputDict
        case 6:
            outputDict = _rotateBottomFace(inputDict, index, location)
            return outputDict
            
            


def _evenCubeCreator(cube):
    betweenFrontAndRight = 9
    betweenRightAndBack = 19
    betweenBackAndLeft = 29
    betweenLeftAndTop = 39
    betweenTopAndBottom = 49
    finalIndex = 59
    
# The purpose of the even cube is to make the modulus work throughout the cube
# This allows me to do % 2 and it still work in the uneven 2 gap between the bottom middle of a face and the top middle of the next face.
    
    cube = cube[:betweenFrontAndRight] + "t" + cube[betweenFrontAndRight:]
    cube = cube[:betweenRightAndBack] + "t" + cube[betweenRightAndBack:]
    cube = cube[:betweenBackAndLeft] + "t" + cube[betweenBackAndLeft:]
    cube = cube[:betweenLeftAndTop] + "t" + cube[betweenLeftAndTop:]
    cube = cube[:betweenTopAndBottom] + "t" + cube[betweenTopAndBottom:]
    cube = cube[:finalIndex] + "t"
    
    return cube


def _realIndexFinder(index):
# Cancels out the added index by the even cube 
    finalFrontIndex = 8  
    insertedIndex1 = 9 
    finalRightIndex = 18
    insertedIndex2 = 19
    finalBackIndex = 28
    insertedIndex3 = 29
    finalLeftIndex = 38
    firstTopIndex = 39
    if index <= finalFrontIndex:
        return index
    
    elif index > insertedIndex1 and index <= finalRightIndex:
        index = index - 1
        return index
    
    elif index > insertedIndex2 and index <= finalBackIndex:
        index = index - 2
        return index
    
    elif index > insertedIndex3  and index <= finalLeftIndex:
        index = index - 3
        return index
    
    elif index > firstTopIndex:
        index = index - 5
        return index

        
def _createDaisy(cube, directions, bottomMiddleColor):
    sideIndicator = 0
    ## Both are different from actual since it is even.
    topFaceStart = 39
    topFaceEnd = 48
    evenCube = _evenCubeCreator(cube)
    modulusRemainder = 0
    distanceBetweenCubes = 2
    for index in range(len(evenCube)):
        evenIndex = index + 1 # all of the numbers we care about are odd. 
        if (evenIndex) % distanceBetweenCubes == modulusRemainder:
            
            if index < topFaceStart or index > topFaceEnd: 
                
                if evenCube[index] == bottomMiddleColor:
                    
                    actualindex = _realIndexFinder(index)
                    outputDict = _rotatetoDaisy(cube, actualindex, sideIndicator)
                    outputDict['dir'] = directions + outputDict['dir']
                    return outputDict
            
            sideIndicator = sideIndicator + 1

                
def _determineFaceIndex(cube, index):
    faceIndex = 1
    for i in range(len(cube)):
        
        if i == index:
            return faceIndex
        
        elif i % 9 == 0 and i != 0:
            faceIndex = faceIndex + 1

            
def _rotateTopOfDaisy(cube):
    inputDict = {}
    inputDict['cube'] = cube
    inputDict['dir'] = 'U'
    
    outputDict = rotate._rotate(inputDict)
    
    outputDict['dir'] = 'U'
    return outputDict

def _determineMatch(cube, index):
    middleIndex = index + 3
    
    if cube[index] == cube[middleIndex]:
        return True
    else:
        return False          

            
def _flipDaisy(cube, bottomMiddleColor):
    
    modulusIndex = 8
    finalIndex = 28
    
    for index in range(len(cube)):
        
        if modulusIndex % 9 == 0:
            
            match = _determineMatch(cube, index)
            
            if match == True:
                
                outputDict = _determineFlip(cube, index, bottomMiddleColor)
                
                if outputDict['dir'] != '':
                    
                    outputDict['flip'] = 1
                    return outputDict
                
                else:
                    outputDict = {}
                    
        elif index > finalIndex:
            
            outputDict = _rotateTopOfDaisy(cube)
            outputDict['flip'] = 0
            return outputDict
        
        modulusIndex = modulusIndex + 1
                

        
def _determineFlip(cube, index, bottomMiddleColor):

    faceIndex = _determineFaceIndex(cube, index)
    
    if faceIndex == 1 and cube[constants.U21] == bottomMiddleColor:
        
        outputDict = _rotateDaisy(cube, 'FF')
        return outputDict
    
    elif faceIndex == 2 and cube[constants.U12] == bottomMiddleColor:
        
        outputDict = _rotateDaisy(cube, 'RR')
        return outputDict
    
    elif faceIndex == 3 and cube[constants.U01] == bottomMiddleColor:
        
        outputDict = _rotateDaisy(cube, 'BB')
        return outputDict
    
    elif faceIndex == 4 and cube[constants.U10] == bottomMiddleColor:
        
        outputDict = _rotateDaisy(cube, 'LL')
        return outputDict
    
    else:
        outputDict = {}
        outputDict['cube'] = cube
        outputDict['dir'] = ''
        return outputDict

    
def _rotateDaisy(cube, direction):
    outputDict = {}
    inputDict = {}
    
    inputDict['cube'] = cube
    inputDict['dir'] = direction
    
    rotatedCube = rotate._rotate(inputDict)
    
    outputDict['cube'] = rotatedCube['cube']
    outputDict['dir'] = direction
    
    return outputDict
    
            
        
    
    