'''
Created on Nov 8, 2022

@author: Tyler Ray
'''

import rubik.cubeConstants as constants



firstSharedEdge = 0
secondSharedEdge = 1
#We can't test for everything, however we can make a few quick for swapped stickers

def _unsolvableCubeDetection(cube):
    unsolvableCubeValidity = _noOppositeShareACube(cube)
    
    return unsolvableCubeValidity



#--------Inner Facing Modules

def _noOppositeShareACube(cube):
    
    distanceToNextCube = 1
    index = constants.F00
    
    while index < constants.lengthOfCube:
        oppositeFaceIndex = _determineOppositeFaceIndex(cube, index)
        sameFaceIndex = _determineSameFaceIndex(cube, index)
        
        if index <= constants.F22:
            validity = _frontFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex)
            
        elif index <= constants.R22:
            validity = _rightFaceOppsoites(cube, index, oppositeFaceIndex, sameFaceIndex)
            
        elif index <= constants.B22:
            validity = _backFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex)
            
        elif index <= constants.L22:
            validity = _leftFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex)
            
        elif index <= constants.U22:
            validity = _upFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex)
            
        else:
            validity = _downFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex)
            
            
        if validity == True:
            
            return validity
        
        index = index + distanceToNextCube
        
    
    return False


def _determineOppositeFaceIndex(cube, index):
    frontFaceMiddleCube = cube[constants.F11]
    rightFaceMiddleCube = cube[constants.R11]
    backFaceMiddleCube = cube[constants.B11]
    leftFaceMiddleCube = cube[constants.L11]
    topFaceMiddleCube = cube[constants.U11]
    downFaceMiddleCube = cube[constants.D11]
    
    cubeColor = cube[index]
        
    if cubeColor == frontFaceMiddleCube:
        oppositeFaceIndex = backFaceMiddleCube 
            
    elif cubeColor == rightFaceMiddleCube:
        oppositeFaceIndex = leftFaceMiddleCube 
            
    elif cubeColor == backFaceMiddleCube:
        oppositeFaceIndex = frontFaceMiddleCube 

    elif cubeColor == leftFaceMiddleCube:
        oppositeFaceIndex = rightFaceMiddleCube 
            
    elif cubeColor == topFaceMiddleCube:
        oppositeFaceIndex = downFaceMiddleCube 
        
    else:
        oppositeFaceIndex = topFaceMiddleCube 
        
    return oppositeFaceIndex

def _determineSameFaceIndex(cube, index):
    frontFaceMiddleCube = cube[constants.F11]
    rightFaceMiddleCube = cube[constants.R11]
    backFaceMiddleCube = cube[constants.B11]
    leftFaceMiddleCube = cube[constants.L11]
    topFaceMiddleCube = cube[constants.U11]
    downFaceMiddleCube = cube[constants.D11]
    
    cubeColor = cube[index]
        
    if cubeColor == frontFaceMiddleCube:
        oppositeFaceIndex = frontFaceMiddleCube 
            
    elif cubeColor == rightFaceMiddleCube:
        oppositeFaceIndex = rightFaceMiddleCube 
            
    elif cubeColor == backFaceMiddleCube:
        oppositeFaceIndex = backFaceMiddleCube 

    elif cubeColor == leftFaceMiddleCube:
        oppositeFaceIndex = leftFaceMiddleCube 

    elif cubeColor == topFaceMiddleCube:
        oppositeFaceIndex = topFaceMiddleCube 
        
    else:
        oppositeFaceIndex = downFaceMiddleCube 
        
    return oppositeFaceIndex



#-----Methods For determining If opposites are on the same cube



def _frontFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex):
    
    if index == constants.F00:
        if cube[F00[firstSharedEdge]] == oppositeFaceIndex or cube[F00[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F01:
        if cube[F01[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F02:
        if cube[F02[firstSharedEdge]] == oppositeFaceIndex or cube[F02[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F10:
        if cube[F10[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F12:
        if cube[F12[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F20:
        if cube[F20[firstSharedEdge]] == oppositeFaceIndex or cube[F20[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F21:
        if cube[F21[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.F22:
        if cube[F22[firstSharedEdge]] == oppositeFaceIndex or cube[F22[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    
    validity = _frontFaceSame(cube, index, sameFaceIndex)
    return validity
        
        
        
def _rightFaceOppsoites(cube, index, oppositeFaceIndex, sameFaceIndex):
    
    if index == constants.R00:
        if cube[R00[firstSharedEdge]] == oppositeFaceIndex or cube[R00[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R01:
        if cube[R01[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R02:
        if cube[R02[firstSharedEdge]] == oppositeFaceIndex or cube[R02[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R10:
        if cube[R10[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R12:
        if cube[R12[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R20:
        if cube[R20[firstSharedEdge]] == oppositeFaceIndex or cube[R20[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R21:
        if cube[R21[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.R22:
        if cube[R22[firstSharedEdge]] == oppositeFaceIndex or cube[R22[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    
    validity = _rightFaceSame(cube, index, sameFaceIndex)
    return validity
    


def _backFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex):
    
    if index == constants.B00:
        if cube[B00[firstSharedEdge]] == oppositeFaceIndex or cube[B00[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B01:
        if cube[B01[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B02:
        if cube[B02[firstSharedEdge]] == oppositeFaceIndex or cube[B02[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B10:
        if cube[B10[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B12:
        if cube[B12[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B20:
        if cube[B20[firstSharedEdge]] == oppositeFaceIndex or cube[B20[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B21:
        if cube[B21[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.B22:
        if cube[B22[firstSharedEdge]] == oppositeFaceIndex or cube[B22[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    
    validity = _frontFaceSame(cube, index, sameFaceIndex)
    return validity
        
        
        
def _leftFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex):
    
    if index == constants.L00:
        if cube[L00[firstSharedEdge]] == oppositeFaceIndex or cube[L00[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L01:
        if cube[L01[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L02:
        if cube[L02[firstSharedEdge]] == oppositeFaceIndex or cube[L02[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L10:
        if cube[L10[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L12:
        if cube[L12[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L20:
        if cube[L20[firstSharedEdge]] == oppositeFaceIndex or cube[L20[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L21:
        if cube[L21[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.L22:
        if cube[L22[firstSharedEdge]] == oppositeFaceIndex or cube[L22[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    
    validity = _leftFaceSame(cube, index, sameFaceIndex)
    return validity
    
    
def _upFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex):
    
    if index == constants.U00:
        if cube[U00[firstSharedEdge]] == oppositeFaceIndex or cube[U00[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U01:
        if cube[U01[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U02:
        if cube[U02[firstSharedEdge]] == oppositeFaceIndex or cube[U02[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U10:
        if cube[U10[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U12:
        if cube[U12[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U20:
        if cube[U20[firstSharedEdge]] == oppositeFaceIndex or cube[U20[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U21:
        if cube[U21[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.U22:
        if cube[U22[firstSharedEdge]] == oppositeFaceIndex or cube[U22[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    
    validity = _topFaceSame(cube, index, sameFaceIndex)
    return validity



def _downFaceOpposites(cube, index, oppositeFaceIndex, sameFaceIndex):
        
    if index == constants.D00:
        if cube[D00[firstSharedEdge]] == oppositeFaceIndex or cube[D00[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D01:
        if cube[D01[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D02:
        if cube[D02[firstSharedEdge]] == oppositeFaceIndex or cube[D02[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D10:
        if cube[D10[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D12:
        if cube[D12[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D20:
        if cube[D20[firstSharedEdge]] == oppositeFaceIndex or cube[D20[secondSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D21:
        if cube[D21[firstSharedEdge]] == oppositeFaceIndex:
            return True
        
    elif index == constants.D22:
        if cube[D22[firstSharedEdge]] == oppositeFaceIndex or cube[D22[secondSharedEdge]] == oppositeFaceIndex:
            return True
        

    validity = _downFaceSame(cube, index, sameFaceIndex)
    return validity










#------Methods for determining if cubes share same face cubes

def _frontFaceSame(cube, index, sameFaceIndex):
    
    if index == constants.F00:
        if cube[F00[firstSharedEdge]] == sameFaceIndex or cube[F00[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F01:
        if cube[F01[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F02:
        if cube[F02[firstSharedEdge]] == sameFaceIndex or cube[F02[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F10:
        if cube[F10[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F12:
        if cube[F12[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F20:
        if cube[F20[firstSharedEdge]] == sameFaceIndex or cube[F20[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F21:
        if cube[F21[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.F22:
        if cube[F22[firstSharedEdge]] == sameFaceIndex or cube[F22[secondSharedEdge]] == sameFaceIndex:
            return True
        
    else:
        return False


def _rightFaceSame(cube, index, sameFaceIndex):
    
    if index == constants.R00:
        if cube[R00[firstSharedEdge]] == sameFaceIndex or cube[R00[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R01:
        if cube[R01[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R02:
        if cube[R02[firstSharedEdge]] == sameFaceIndex or cube[R02[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R10:
        if cube[R10[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R12:
        if cube[R12[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R20:
        if cube[R20[firstSharedEdge]] == sameFaceIndex or cube[R20[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R21:
        if cube[R21[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.R22:
        if cube[R22[firstSharedEdge]] == sameFaceIndex or cube[R22[secondSharedEdge]] == sameFaceIndex:
            return True
        
    else:
        return False
    
    
def _backFaceSame(cube, index, sameFaceIndex):

    if index == constants.B00:
        if cube[B00[firstSharedEdge]] == sameFaceIndex or cube[B00[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B01:
        if cube[B01[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B02:
        if cube[B02[firstSharedEdge]] == sameFaceIndex or cube[B02[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B10:
        if cube[B10[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B12:
        if cube[B12[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B20:
        if cube[B20[firstSharedEdge]] == sameFaceIndex or cube[B20[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B21:
        if cube[B21[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.B22:
        if cube[B22[firstSharedEdge]] == sameFaceIndex or cube[B22[secondSharedEdge]] == sameFaceIndex:
            return True
        
    else:
        return False
    
    
def _leftFaceSame(cube, index, sameFaceIndex):

    if index == constants.L00:
        if cube[L00[firstSharedEdge]] == sameFaceIndex or cube[L00[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L01:
        if cube[L01[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L02:
        if cube[L02[firstSharedEdge]] == sameFaceIndex or cube[L02[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L10:
        if cube[L10[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L12:
        if cube[L12[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L20:
        if cube[L20[firstSharedEdge]] == sameFaceIndex or cube[L20[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L21:
        if cube[L21[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.L22:
        if cube[L22[firstSharedEdge]] == sameFaceIndex or cube[L22[secondSharedEdge]] == sameFaceIndex:
            return True
        
    else:
        return False
    
    
def _topFaceSame(cube, index, sameFaceIndex):

    if index == constants.U00:
        if cube[U00[firstSharedEdge]] == sameFaceIndex or cube[U00[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U01:
        if cube[U01[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U02:
        if cube[U02[firstSharedEdge]] == sameFaceIndex or cube[U02[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U10:
        if cube[U10[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U12:
        if cube[U12[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U20:
        if cube[U20[firstSharedEdge]] == sameFaceIndex or cube[U20[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U21:
        if cube[U21[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.U22:
        if cube[U22[firstSharedEdge]] == sameFaceIndex or cube[U22[secondSharedEdge]] == sameFaceIndex:
            return True
        
    else:
        return False


def _downFaceSame(cube, index, sameFaceIndex):
    
    if index == constants.D00:
        if cube[D00[firstSharedEdge]] == sameFaceIndex or cube[D00[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D01:
        if cube[D01[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D02:
        if cube[D02[firstSharedEdge]] == sameFaceIndex or cube[D02[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D10:
        if cube[D10[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D12:
        if cube[D12[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D20:
        if cube[D20[firstSharedEdge]] == sameFaceIndex or cube[D20[secondSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D21:
        if cube[D21[firstSharedEdge]] == sameFaceIndex:
            return True
        
    elif index == constants.D22:
        if cube[D22[firstSharedEdge]] == sameFaceIndex or cube[D22[secondSharedEdge]] == sameFaceIndex:
            return True
        
    else:
        return False


    


    
#--------Cubes and their corresponding other sides

#First part is index location, first and second numbers are shared sides

F00 = [constants.L02, constants.U20]
F01 = [constants.U21]
F02 = [constants.U22, constants.R00]
F10 = [constants.L12]
F12 = [constants.R10]
F20 = [constants.D00, constants.L22]
F21 = [constants.D01]
F22 = [constants.R20, constants.D02]

R00 = [constants.F02, constants.U22]
R01 = [constants.U12]
R02 = [constants.U02, constants.B00]
R10 = [constants.F12]
R12 = [constants.B10]
R20 = [constants.D02, constants.F22]
R21 = [constants.D12]
R22 = [constants.D22, constants.B20]

# Back Face
B00 = [constants.U02, constants.R02]
B01 = [constants.U01]
B02 = [constants.U00, constants.L00]
B10 = [constants.R12]
B12 = [constants.L10]
B20 = [constants.R22, constants.D22]
B21 = [constants.D21]
B22 = [constants.D20, constants.L20]

# Left Face
L00 = [constants.B02, constants.U00]
L01 = [constants.U10]
L02 = [constants.U20, constants.F00]
L10 = [constants.B12]
L12 = [constants.F10]
L20 = [constants.B22, constants.D20]
L21 = [constants.D10]
L22 = [constants.F20, constants.D00]

# Upper Face
U00 = [constants.L00, constants.B02]
U01 = [constants.B01]
U02 = [constants.B00, constants.R02]
U10 = [constants.L01]
U12 = [constants.R01]
U20 = [constants.F00, constants.L02]
U21 = [constants.F01]
U22 = [constants.F02, constants.R00]

# Downward Face
D00 = [constants.F20, constants.L22]
D01 = [constants.F21]
D02 = [constants.F22, constants.R20]
D10 = [constants.L21]
D12 = [constants.R21]
D20 = [constants.L20, constants.B22]
D21 = [constants.B21]
D22 = [constants.B20, constants.R22]


            
    
    