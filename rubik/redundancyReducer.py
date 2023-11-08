'''
Created on Oct 11, 2022

@author: Tyler Ray
'''

def _redundancyReducer(rotations):
    
    rotations = _oppositeDoubleMovesRemover(rotations)
    rotations = _oppositeMovesRemover(rotations)
    
    rotations = _uppercaseURemover(rotations)
    rotations = _lowercaseuRemover(rotations)
    
    rotations = _lowercasefRemover(rotations)
    rotations = _uppercaseFRemover(rotations)
    
    rotations = _lowercaserRemover(rotations)
    rotations = _uppercaseRRemover(rotations)
    
    rotations = _lowercasebRemover(rotations)
    rotations = _uppercaseBRemover(rotations)
    
    rotations = _lowercaselRemover(rotations)
    rotations = _uppercaseLRemover(rotations)
    
    rotations = _lowercasedRemover(rotations)
    rotations = _uppercaseDRemover(rotations)

    rotations = rotations.replace(' ', '')
    
    return rotations




def _uppercaseURemover(rotations):
    
    rotations = rotations.replace('UUUU', '')
    rotations = rotations.replace('UUU', 'u')
    return rotations
    
    
def _lowercaseuRemover(rotations):
    
    rotations = rotations.replace('uuuu', '')
    rotations = rotations.replace('uuu', 'U')
    return rotations
        
def _lowercaselRemover(rotations):
    
    rotations = rotations.replace('llll', '')
    rotations = rotations.replace('lll', 'L')
    return rotations

def _uppercaseLRemover(rotations):
    
    rotations = rotations.replace('LLLL', '')
    rotations = rotations.replace('LLL', 'l')
    return rotations

def _lowercasefRemover(rotations):
    
    rotations = rotations.replace('ffff', '')
    rotations = rotations.replace('fff', 'F')
    return rotations

def _uppercaseFRemover(rotations):
    
    rotations = rotations.replace('FFFF', '')
    rotations = rotations.replace('FFF', 'f')
    return rotations


def _lowercasebRemover(rotations):
    
    rotations = rotations.replace('bbbb', '')
    rotations = rotations.replace('bbb', 'B')
    return rotations

def _uppercaseBRemover(rotations):
    
    rotations = rotations.replace('BBBB', '')
    rotations = rotations.replace('BBB', 'b')
    return rotations


def _lowercaserRemover(rotations):
    
    rotations = rotations.replace('rrrr', '')
    rotations = rotations.replace('rrr', 'R')
    return rotations

def _uppercaseRRemover(rotations):
    
    rotations = rotations.replace('RRRR', '')
    rotations = rotations.replace('RRR', 'r')
    return rotations

def _lowercasedRemover(rotations):
    
    rotations = rotations.replace('dddd', '')
    rotations = rotations.replace('ddd', 'D')
    return rotations

def _uppercaseDRemover(rotations):
    
    rotations = rotations.replace('DDDD', '')
    rotations = rotations.replace('DDD', 'd')
    return rotations


def _oppositeMovesRemover(rotations):
    
    rotations = rotations.replace('Uu', '')
    rotations = rotations.replace('uU', '')
    
    rotations = rotations.replace('Ff', '')
    rotations = rotations.replace('fF', '')
    
    rotations = rotations.replace('Rr', '')
    rotations = rotations.replace('rR', '')
    
    rotations = rotations.replace('Bb', '')
    rotations = rotations.replace('bB', '')
    
    rotations = rotations.replace('Ll', '')
    rotations = rotations.replace('lL', '')
    
    rotations = rotations.replace('Dd', '')
    rotations = rotations.replace('dD', '')
    
    return rotations


def _oppositeDoubleMovesRemover(rotations):
    rotations = rotations.replace('UUuu', '')
    rotations = rotations.replace('uuUU', '')
    
    rotations = rotations.replace('FFff', '')
    rotations = rotations.replace('ffFF', '')
    
    rotations = rotations.replace('RRrr', '')
    rotations = rotations.replace('rrRR', '')
    
    rotations = rotations.replace('BBbb', '')
    rotations = rotations.replace('bbBB', '')
    
    rotations = rotations.replace('LLll', '')
    rotations = rotations.replace('llLL', '')
    
    rotations = rotations.replace('DDdd', '')
    rotations = rotations.replace('ddDD', '')
    
    return rotations
    
    