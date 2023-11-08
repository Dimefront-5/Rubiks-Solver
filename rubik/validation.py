'''
Created on Sep 13, 2022

@author: Tyler Ray
'''
import re
import rubik.cubeConstants as constants

def _validation(parms):
    outputDict = {}
    outputDict['status'] = 'ok'
    cube = parms
    status = _cubeValidity(cube)
    return status


def _cubeValidity(cube):
    if cube == None :
        return 'error: invalid cube, must present a cube'
    
    elif cube == '' :
        return 'error: invalid cube, must present a cube'
    
    elif len(cube) != constants.lengthOfCube :
        return 'error: invalid cube, must be exactly 54 characters'
    
    else :
        if bool(re.match('^[brogwy]*$', cube)) == False:
            return 'error: invalid cube, must contain characters of brogwy meaning blue, red, orange, green, white, yellow'
        status = _colorCount(cube)
        if status != None:
            return status
        status = _validMiddleCubes(cube)
        if status != None:
            return status
        return 'ok'
    
    
def _colorCount(cube):
    redCount = 0
    blueCount = 0
    greenCount = 0
    yellowCount = 0
    orangeCount = 0
    whiteCount = 0
    
    for element in cube :
        match element:
                case 'r' :
                    redCount = redCount + 1
                    if redCount > 9 :
                        return "error: invalid cube, there must be exactly 9 spaces of each color" 
                    
                case 'b' :
                    blueCount = blueCount + 1
                    if blueCount > 9 :
                        return "error: invalid cube, there must be exactly 9 spaces of each color" 
                    
                case 'g' :
                    greenCount = greenCount + 1
                    if greenCount > 9 :
                        return "error: invalid cube, there must be exactly 9 spaces of each color" 
                    
                case 'y' :
                    yellowCount = yellowCount + 1
                    if yellowCount > 9 :
                        return "error: invalid cube, there must be exactly 9 spaces of each color" 
                    
                case 'w' :
                    whiteCount = whiteCount + 1
                    if whiteCount > 9 :
                        return "error: invalid cube, there must be exactly 9 spaces of each color" 
                    
                case 'o' :
                    orangeCount = orangeCount + 1
                    if orangeCount > 9 :
                        return "error: invalid cube, there must be exactly 9 spaces of each color" 


def _validMiddleCubes(cube):
    # This indicates whether a color has been found in a middle piece.
    previousRed = False
    previousBlue = False
    previousGreen = False
    previousYellow = False
    previousWhite = False
    previousOrange = False
    
    index = 5 # Start our index at 5 because our middle pieces start at index 4.
    for element in cube : #Iterates through Cube, when it reaches a middle piece, reads in color, and sees if it has already appeared.
        if index % 9 == 0 :
            match element:
                case 'r' :
                    if previousRed == False :
                        previousRed = True
                    else :
                        return "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
                    
                case 'b' :
                    if previousBlue == False :
                        previousBlue = True
                    else :
                        return "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
                    
                case 'g' :
                    if previousGreen == False :
                        previousGreen = True
                    else :
                        return "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
                    
                case 'y' :
                    if previousYellow == False :
                        previousYellow = True
                    else :
                        return "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
                    
                case 'w' :
                    if previousWhite == False :
                        previousWhite = True
                    else :
                        return "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
                    
                case 'o' :
                    if previousOrange == False :
                        previousOrange = True
                    else :
                        return "error: invalid cube, rubik's cubes cannot contain two middle pieces of the same color"
                    
        
        index = index + 1