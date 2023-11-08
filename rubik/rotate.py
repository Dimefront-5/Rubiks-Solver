'''
Created on Aug 30, 2022

@author: Tyler Ray
'''
import re
import rubik.validation as validation
import rubik.cubeConstants as constants


# Will return the rotated Cube, or an error if the cube is invalid
def _rotate(parms):
    result = {} 
    
    cube = parms.get('cube')
    status = validation._validation(cube)
    
    # If cube's status is anything, this means it is an error.
    if status != 'ok':
        result['status'] = status
        return result
    
    
    direction = parms.get('dir')
    direction = _validDir(direction)
    if direction == "Invalid" :
        result['status'] = "error: invalid rotation, must be a rotation of F,f,R,r,B,b,L,l,U,u,D,d"
        return result
    
    
    for element in direction :
        rotatedCube = _evaluateDir(element, cube)
        cube = rotatedCube
        
    result['cube'] = rotatedCube
    result['status'] = 'ok'  
                       
    return result


# ------- Inward facing modules


def _validDir(direction):
    if ((direction == "") or direction == None) :
        direction = 'F'
        
    else :
        if bool(re.match('^[FfRrBbLlUuDd]*$', direction)) == False:
            return "Invalid"
        
    return direction

def _evaluateDir(direction, cube):
    rotatedCube = {}
    
    match direction:
            case 'F':
                rotatedCube = _rotate_F(cube)
                direction[1 : len(direction)]
                
            case 'f':
                rotatedCube = _rotate_f(cube)
                direction[1 : len(direction)]
                
            case 'R':
                rotatedCube = _rotate_R(cube)
                direction[1 : len(direction)]
                
            case 'r':
                rotatedCube = _rotate_r(cube)
                direction[1 : len(direction)]
                
            case 'B':
                rotatedCube = _rotate_B(cube)
                direction[1 : len(direction)]
                
            case 'b':
                rotatedCube = _rotate_b(cube)
                direction[1 : len(direction)]
                
            case 'L':
                rotatedCube = _rotate_L(cube)
                direction[1: len(direction)]
                
            case 'l' :
                rotatedCube = _rotate_l(cube)
                direction[1: len(direction)]
                
            case 'U':
                rotatedCube = _rotate_U(cube)
                direction[1: len(direction)]
                
            case 'u':
                rotatedCube = _rotate_u(cube)
                direction[1: len(direction)]
                
            case 'D':
                rotatedCube = _rotate_D(cube)
                direction[1: len(direction)]
                
            case 'd':
                rotatedCube = _rotate_d(cube)
                direction[1: len(direction)]
                
    return rotatedCube


def _rotate_F(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    #rotate front face
    rotatedCubeList[constants.F02] = cubeList[constants.F00]
    rotatedCubeList[constants.F12] = cubeList[constants.F01]
    rotatedCubeList[constants.F22] = cubeList[constants.F02]
    rotatedCubeList[constants.F01] = cubeList[constants.F10]
    rotatedCubeList[constants.F11] = cubeList[constants.F11]
    rotatedCubeList[constants.F21] = cubeList[constants.F12]
    rotatedCubeList[constants.F00] = cubeList[constants.F20]
    rotatedCubeList[constants.F10] = cubeList[constants.F21]
    rotatedCubeList[constants.F20] = cubeList[constants.F22]
    
    #rotate top to right
    rotatedCubeList[constants.R00] = cubeList[constants.U20]
    rotatedCubeList[constants.R10] = cubeList[constants.U21]
    rotatedCubeList[constants.R20] = cubeList[constants.U22]
    
    #rotate right to bottom
    rotatedCubeList[constants.D02] = cubeList[constants.R00]
    rotatedCubeList[constants.D01] = cubeList[constants.R10]
    rotatedCubeList[constants.D00] = cubeList[constants.R20]
    
    #rotate bottom to left
    rotatedCubeList[constants.L02] = cubeList[constants.D00]
    rotatedCubeList[constants.L12] = cubeList[constants.D01]
    rotatedCubeList[constants.L22] = cubeList[constants.D02]
    
    #rotate left to top
    rotatedCubeList[constants.U22] = cubeList[constants.L02]
    rotatedCubeList[constants.U21] = cubeList[constants.L12]
    rotatedCubeList[constants.U20] = cubeList[constants.L22]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_f(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    #rotate front face
    rotatedCubeList[constants.F02] = cubeList[constants.F22]
    rotatedCubeList[constants.F12] = cubeList[constants.F21]
    rotatedCubeList[constants.F22] = cubeList[constants.F20]
    rotatedCubeList[constants.F01] = cubeList[constants.F12]
    rotatedCubeList[constants.F11] = cubeList[constants.F11]
    rotatedCubeList[constants.F21] = cubeList[constants.F10]
    rotatedCubeList[constants.F00] = cubeList[constants.F02]
    rotatedCubeList[constants.F10] = cubeList[constants.F01]
    rotatedCubeList[constants.F20] = cubeList[constants.F00]
    
    #rotate bottom to right
    rotatedCubeList[constants.R00] = cubeList[constants.D02]
    rotatedCubeList[constants.R10] = cubeList[constants.D01]
    rotatedCubeList[constants.R20] = cubeList[constants.D00]
    
    #rotate left to bottom
    rotatedCubeList[constants.D02] = cubeList[constants.L22]
    rotatedCubeList[constants.D01] = cubeList[constants.L12]
    rotatedCubeList[constants.D00] = cubeList[constants.L02]
    
    #rotate top to left
    rotatedCubeList[constants.L02] = cubeList[constants.U22]
    rotatedCubeList[constants.L12] = cubeList[constants.U21]
    rotatedCubeList[constants.L22] = cubeList[constants.U20]
    
    #rotate right to top
    rotatedCubeList[constants.U22] = cubeList[constants.R20]
    rotatedCubeList[constants.U21] = cubeList[constants.R10]
    rotatedCubeList[constants.U20] = cubeList[constants.R00]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_R(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    #rotate right face
    rotatedCubeList[constants.R02] = cubeList[constants.R00]
    rotatedCubeList[constants.R12] = cubeList[constants.R01]
    rotatedCubeList[constants.R22] = cubeList[constants.R02]
    rotatedCubeList[constants.R01] = cubeList[constants.R10]
    rotatedCubeList[constants.R11] = cubeList[constants.R11]
    rotatedCubeList[constants.R21] = cubeList[constants.R12]
    rotatedCubeList[constants.R00] = cubeList[constants.R20]
    rotatedCubeList[constants.R10] = cubeList[constants.R21]
    rotatedCubeList[constants.R20] = cubeList[constants.R22]
    
    #rotate front to top
    rotatedCubeList[constants.U02] = cubeList[constants.F02]
    rotatedCubeList[constants.U12] = cubeList[constants.F12]
    rotatedCubeList[constants.U22] = cubeList[constants.F22]
    
    #rotate top to back
    rotatedCubeList[constants.B20] = cubeList[constants.U02]
    rotatedCubeList[constants.B10] = cubeList[constants.U12]
    rotatedCubeList[constants.B00] = cubeList[constants.U22]
    
    #rotate back to bottom
    rotatedCubeList[constants.D02] = cubeList[constants.B20]
    rotatedCubeList[constants.D12] = cubeList[constants.B10]
    rotatedCubeList[constants.D22] = cubeList[constants.B00]
    
    #rotate bottom to front
    rotatedCubeList[constants.F02] = cubeList[constants.D02]
    rotatedCubeList[constants.F12] = cubeList[constants.D12]
    rotatedCubeList[constants.F22] = cubeList[constants.D22]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_B(cube): 
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate back face
    rotatedCubeList[constants.B02] = cubeList[constants.B00]
    rotatedCubeList[constants.B12] = cubeList[constants.B01]
    rotatedCubeList[constants.B22] = cubeList[constants.B02]
    rotatedCubeList[constants.B01] = cubeList[constants.B10]
    rotatedCubeList[constants.B11] = cubeList[constants.B11]
    rotatedCubeList[constants.B21] = cubeList[constants.B12]
    rotatedCubeList[constants.B00] = cubeList[constants.B20]
    rotatedCubeList[constants.B10] = cubeList[constants.B21]
    rotatedCubeList[constants.B20] = cubeList[constants.B22]
    
    #rotate top to left
    rotatedCubeList[constants.L20] = cubeList[constants.U00]
    rotatedCubeList[constants.L10] = cubeList[constants.U01]
    rotatedCubeList[constants.L00] = cubeList[constants.U02]
    
    #rotate left to bottom
    rotatedCubeList[constants.D22] = cubeList[constants.L20]
    rotatedCubeList[constants.D21] = cubeList[constants.L10]
    rotatedCubeList[constants.D20] = cubeList[constants.L00]
    
    #rotate bottom to right
    rotatedCubeList[constants.R22] = cubeList[constants.D20]
    rotatedCubeList[constants.R12] = cubeList[constants.D21]
    rotatedCubeList[constants.R02] = cubeList[constants.D22]
    
    #rotate right to top
    rotatedCubeList[constants.U00] = cubeList[constants.R02]
    rotatedCubeList[constants.U01] = cubeList[constants.R12]
    rotatedCubeList[constants.U02] = cubeList[constants.R22]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_r(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    #rotate right face
    rotatedCubeList[constants.R20] = cubeList[constants.R00]
    rotatedCubeList[constants.R10] = cubeList[constants.R01]
    rotatedCubeList[constants.R00] = cubeList[constants.R02]
    rotatedCubeList[constants.R21] = cubeList[constants.R10]
    rotatedCubeList[constants.R11] = cubeList[constants.R11]
    rotatedCubeList[constants.R01] = cubeList[constants.R12]
    rotatedCubeList[constants.R22] = cubeList[constants.R20]
    rotatedCubeList[constants.R12] = cubeList[constants.R21]
    rotatedCubeList[constants.R02] = cubeList[constants.R22]
    
    #rotate front to bottom
    rotatedCubeList[constants.D02] = cubeList[constants.F02]
    rotatedCubeList[constants.D12] = cubeList[constants.F12]
    rotatedCubeList[constants.D22] = cubeList[constants.F22]
    
    #rotate top to front
    rotatedCubeList[constants.F22] = cubeList[constants.U22]
    rotatedCubeList[constants.F12] = cubeList[constants.U12]
    rotatedCubeList[constants.F02] = cubeList[constants.U02]
    
    #rotate back to top
    rotatedCubeList[constants.U02] = cubeList[constants.B20]
    rotatedCubeList[constants.U12] = cubeList[constants.B10]
    rotatedCubeList[constants.U22] = cubeList[constants.B00]
    
    #rotate bottom to back
    rotatedCubeList[constants.B00] = cubeList[constants.D22]
    rotatedCubeList[constants.B10] = cubeList[constants.D12]
    rotatedCubeList[constants.B20] = cubeList[constants.D02]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_b(cube): 
    
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate back face
    rotatedCubeList[constants.B20] = cubeList[constants.B00]
    rotatedCubeList[constants.B10] = cubeList[constants.B01]
    rotatedCubeList[constants.B00] = cubeList[constants.B02]
    rotatedCubeList[constants.B21] = cubeList[constants.B10]
    rotatedCubeList[constants.B11] = cubeList[constants.B11]
    rotatedCubeList[constants.B01] = cubeList[constants.B12]
    rotatedCubeList[constants.B22] = cubeList[constants.B20]
    rotatedCubeList[constants.B12] = cubeList[constants.B21]
    rotatedCubeList[constants.B02] = cubeList[constants.B22]
    
    #rotate top to right
    rotatedCubeList[constants.R02] = cubeList[constants.U00]
    rotatedCubeList[constants.R12] = cubeList[constants.U01]
    rotatedCubeList[constants.R22] = cubeList[constants.U02]
    
    #rotate right to bottom
    rotatedCubeList[constants.D20] = cubeList[constants.R22]
    rotatedCubeList[constants.D21] = cubeList[constants.R12]
    rotatedCubeList[constants.D22] = cubeList[constants.R02]
    
    #rotate bottom to left
    rotatedCubeList[constants.L00] = cubeList[constants.D20]
    rotatedCubeList[constants.L10] = cubeList[constants.D21]
    rotatedCubeList[constants.L20] = cubeList[constants.D22]
    
    #rotate left to top
    rotatedCubeList[constants.U00] = cubeList[constants.L20]
    rotatedCubeList[constants.U01] = cubeList[constants.L10]
    rotatedCubeList[constants.U02] = cubeList[constants.L00]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_L(cube): 
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate left face
    rotatedCubeList[constants.L02] = cubeList[constants.L00]
    rotatedCubeList[constants.L12] = cubeList[constants.L01]
    rotatedCubeList[constants.L22] = cubeList[constants.L02]
    rotatedCubeList[constants.L01] = cubeList[constants.L10]
    rotatedCubeList[constants.L11] = cubeList[constants.L11]
    rotatedCubeList[constants.L21] = cubeList[constants.L12]
    rotatedCubeList[constants.L00] = cubeList[constants.L20]
    rotatedCubeList[constants.L10] = cubeList[constants.L21]
    rotatedCubeList[constants.L20] = cubeList[constants.L22]
    
    #rotate front to bottom
    rotatedCubeList[constants.D00] = cubeList[constants.F00]
    rotatedCubeList[constants.D10] = cubeList[constants.F10]
    rotatedCubeList[constants.D20] = cubeList[constants.F20]
    
    #rotate bottom to back
    rotatedCubeList[constants.B22] = cubeList[constants.D00]
    rotatedCubeList[constants.B12] = cubeList[constants.D10]
    rotatedCubeList[constants.B02] = cubeList[constants.D20]
    
    #rotate back to top
    rotatedCubeList[constants.U20] = cubeList[constants.B02]
    rotatedCubeList[constants.U10] = cubeList[constants.B12]
    rotatedCubeList[constants.U00] = cubeList[constants.B22]
    
    #rotate top to front
    rotatedCubeList[constants.F20] = cubeList[constants.U20]
    rotatedCubeList[constants.F10] = cubeList[constants.U10]
    rotatedCubeList[constants.F00] = cubeList[constants.U00]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_l(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate left face
    rotatedCubeList[constants.L20] = cubeList[constants.L00]
    rotatedCubeList[constants.L10] = cubeList[constants.L01]
    rotatedCubeList[constants.L00] = cubeList[constants.L02]
    rotatedCubeList[constants.L21] = cubeList[constants.L10]
    rotatedCubeList[constants.L11] = cubeList[constants.L11]
    rotatedCubeList[constants.L01] = cubeList[constants.L12]
    rotatedCubeList[constants.L22] = cubeList[constants.L20]
    rotatedCubeList[constants.L12] = cubeList[constants.L21]
    rotatedCubeList[constants.L02] = cubeList[constants.L22]
    
    #rotate front to top
    rotatedCubeList[constants.U00] = cubeList[constants.F00]
    rotatedCubeList[constants.U10] = cubeList[constants.F10]
    rotatedCubeList[constants.U20] = cubeList[constants.F20]
    
    #rotate top to back
    rotatedCubeList[constants.B22] = cubeList[constants.U00]
    rotatedCubeList[constants.B12] = cubeList[constants.U10]
    rotatedCubeList[constants.B02] = cubeList[constants.U20]
    
    #rotate back to bottom
    rotatedCubeList[constants.D20] = cubeList[constants.B02]
    rotatedCubeList[constants.D10] = cubeList[constants.B12]
    rotatedCubeList[constants.D00] = cubeList[constants.B22]
    
    #rotate bottom to front
    rotatedCubeList[constants.F20] = cubeList[constants.D20]
    rotatedCubeList[constants.F10] = cubeList[constants.D10]
    rotatedCubeList[constants.F00] = cubeList[constants.D00]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_U(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate top face
    rotatedCubeList[constants.U02] = cubeList[constants.U00]
    rotatedCubeList[constants.U12] = cubeList[constants.U01]
    rotatedCubeList[constants.U22] = cubeList[constants.U02]
    rotatedCubeList[constants.U01] = cubeList[constants.U10]
    rotatedCubeList[constants.U11] = cubeList[constants.U11]
    rotatedCubeList[constants.U21] = cubeList[constants.U12]
    rotatedCubeList[constants.U00] = cubeList[constants.U20]
    rotatedCubeList[constants.U10] = cubeList[constants.U21]
    rotatedCubeList[constants.U20] = cubeList[constants.U22]
    
    #rotate front to left
    rotatedCubeList[constants.L00] = cubeList[constants.F00]
    rotatedCubeList[constants.L01] = cubeList[constants.F01]
    rotatedCubeList[constants.L02] = cubeList[constants.F02]
    
    #rotate left to back
    rotatedCubeList[constants.B00] = cubeList[constants.L00]
    rotatedCubeList[constants.B01] = cubeList[constants.L01]
    rotatedCubeList[constants.B02] = cubeList[constants.L02]
    
    #rotate back to right
    rotatedCubeList[constants.R00] = cubeList[constants.B00]
    rotatedCubeList[constants.R01] = cubeList[constants.B01]
    rotatedCubeList[constants.R02] = cubeList[constants.B02]
    
    #rotate right to front
    rotatedCubeList[constants.F02] = cubeList[constants.R02]
    rotatedCubeList[constants.F01] = cubeList[constants.R01]
    rotatedCubeList[constants.F00] = cubeList[constants.R00]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_u(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate top face
    rotatedCubeList[constants.U20] = cubeList[constants.U00]
    rotatedCubeList[constants.U10] = cubeList[constants.U01]
    rotatedCubeList[constants.U00] = cubeList[constants.U02]
    rotatedCubeList[constants.U21] = cubeList[constants.U10]
    rotatedCubeList[constants.U11] = cubeList[constants.U11]
    rotatedCubeList[constants.U01] = cubeList[constants.U12]
    rotatedCubeList[constants.U22] = cubeList[constants.U20]
    rotatedCubeList[constants.U12] = cubeList[constants.U21]
    rotatedCubeList[constants.U02] = cubeList[constants.U22]
    
    #rotate front to right
    rotatedCubeList[constants.R00] = cubeList[constants.F00]
    rotatedCubeList[constants.R01] = cubeList[constants.F01]
    rotatedCubeList[constants.R02] = cubeList[constants.F02]
    
    #rotate right to back
    rotatedCubeList[constants.B00] = cubeList[constants.R00]
    rotatedCubeList[constants.B01] = cubeList[constants.R01]
    rotatedCubeList[constants.B02] = cubeList[constants.R02]
    
    #rotate back to left
    rotatedCubeList[constants.L02] = cubeList[constants.B02]
    rotatedCubeList[constants.L01] = cubeList[constants.B01]
    rotatedCubeList[constants.L00] = cubeList[constants.B00]
    
    #rotate left to front
    rotatedCubeList[constants.F02] = cubeList[constants.L02]
    rotatedCubeList[constants.F01] = cubeList[constants.L01]
    rotatedCubeList[constants.F00] = cubeList[constants.L00]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_D(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate bottom face
    rotatedCubeList[constants.D02] = cubeList[constants.D00]
    rotatedCubeList[constants.D12] = cubeList[constants.D01]
    rotatedCubeList[constants.D22] = cubeList[constants.D02]
    rotatedCubeList[constants.D01] = cubeList[constants.D10]
    rotatedCubeList[constants.D11] = cubeList[constants.D11]
    rotatedCubeList[constants.D21] = cubeList[constants.D12]
    rotatedCubeList[constants.D00] = cubeList[constants.D20]
    rotatedCubeList[constants.D10] = cubeList[constants.D21]
    rotatedCubeList[constants.D20] = cubeList[constants.D22]
    
    #rotate front to right
    rotatedCubeList[constants.R20] = cubeList[constants.F20]
    rotatedCubeList[constants.R21] = cubeList[constants.F21]
    rotatedCubeList[constants.R22] = cubeList[constants.F22]
    
    #rotate right to back
    rotatedCubeList[constants.B20] = cubeList[constants.R20]
    rotatedCubeList[constants.B21] = cubeList[constants.R21]
    rotatedCubeList[constants.B22] = cubeList[constants.R22]
    
    #rotate back to left
    rotatedCubeList[constants.L20] = cubeList[constants.B20]
    rotatedCubeList[constants.L21] = cubeList[constants.B21]
    rotatedCubeList[constants.L22] = cubeList[constants.B22]
    
    #rotate left to front
    rotatedCubeList[constants.F20] = cubeList[constants.L20]
    rotatedCubeList[constants.F21] = cubeList[constants.L21]
    rotatedCubeList[constants.F22] = cubeList[constants.L22]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube

def _rotate_d(cube):
    cubeList = list(cube)
    rotatedCubeList = cubeList[:]
    
    #rotate bottom face
    rotatedCubeList[constants.D20] = cubeList[constants.D00]
    rotatedCubeList[constants.D10] = cubeList[constants.D01]
    rotatedCubeList[constants.D00] = cubeList[constants.D02]
    rotatedCubeList[constants.D21] = cubeList[constants.D10]
    rotatedCubeList[constants.D11] = cubeList[constants.D11]
    rotatedCubeList[constants.D01] = cubeList[constants.D12]
    rotatedCubeList[constants.D22] = cubeList[constants.D20]
    rotatedCubeList[constants.D12] = cubeList[constants.D21]
    rotatedCubeList[constants.D02] = cubeList[constants.D22]
    
    #rotate front to left
    rotatedCubeList[constants.L20] = cubeList[constants.F20]
    rotatedCubeList[constants.L21] = cubeList[constants.F21]
    rotatedCubeList[constants.L22] = cubeList[constants.F22]
    
    #rotate left to back
    rotatedCubeList[constants.B20] = cubeList[constants.L20]
    rotatedCubeList[constants.B21] = cubeList[constants.L21]
    rotatedCubeList[constants.B22] = cubeList[constants.L22]
    
    #rotate back to right
    rotatedCubeList[constants.R20] = cubeList[constants.B20]
    rotatedCubeList[constants.R21] = cubeList[constants.B21]
    rotatedCubeList[constants.R22] = cubeList[constants.B22]
    
    #rotate right to front
    rotatedCubeList[constants.F20] = cubeList[constants.R20]
    rotatedCubeList[constants.F21] = cubeList[constants.R21]
    rotatedCubeList[constants.F22] = cubeList[constants.R22]
    
    rotatedCube = "".join(rotatedCubeList)
    return rotatedCube