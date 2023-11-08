'''
Created on Oct 24, 2022

@author: Tyler Ray
'''
import rubik.rotate as rotate

def _rotateCommunicator(cube, directions): 
    
    inputDict = {}   
    inputDict['cube'] = cube
    inputDict['dir'] = directions
    outputDict = rotate._rotate(inputDict)
    cube = outputDict['cube']
    
    return cube