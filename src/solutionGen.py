import os
from hashlib import sha256

def solutionGen():
    targetPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'target.txt')
    inputPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'input.txt')
    solutionPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'solution.txt')
    
    target = open(targetPath, 'r').read()
    input = open(inputPath, 'r').read()
    
    i = 0
    while True:
        newInput = input + str(i)
        hex = sha256(newInput.encode()).hexdigest()
        binary = bin(int(hex, 16))[2:].zfill(256)
        i += 1
        if binary <= target:
            open(solutionPath, 'w').write(newInput[9:])
            print("Solution Generated: " + newInput[9:])
            return newInput