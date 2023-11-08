'''
Created on Oct 25, 2022

@author: Tyler Ray
'''

import hashlib
import random

def _integrityToken(cube, rotations):
    hashinput = cube + rotations
    sha256Hash = hashlib.sha256()
    sha256Hash.update(hashinput.encode())
    
    fullToken = sha256Hash.hexdigest()
    
    returnToken = _hashRandomizer(fullToken)
    
    return returnToken



def _hashRandomizer(hashinput):
    startIndexOfHash = 0
    endIndexOfHash = len(hashinput)
    lastIndexOfFirstDigit = endIndexOfHash - 8
    lengthOfSubstringToken = 8
    
    randomStart = random.randint(startIndexOfHash, lastIndexOfFirstDigit)
    
    randomEnd = randomStart + lengthOfSubstringToken
    
    output = hashinput[randomStart:randomEnd]
    
    
    return output
        
                        
    
    