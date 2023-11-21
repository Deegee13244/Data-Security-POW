import os
from hashlib import sha256

def solutionGen():
    #constructing file paths
    targetPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'target.txt')
    inputPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'input.txt')
    solutionPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'solution.txt')
    
    #reading contents
    target = open(targetPath, 'r').read()
    input = open(inputPath, 'r').read()
    
    i = 0
    while True:
        #concatinate counter to the original input
        newInput = input + str(i)
        
        #caluclate hash of newInput
        hex = sha256(newInput.encode()).hexdigest()
        
        #convert the hex hash to binary and make it 256 bits long
        binary = bin(int(hex, 16))[2:].zfill(256)
        
        i += 1
        
        #see if binary has is equal to target
        if binary == target:
            open(solutionPath, 'w').write(newInput[9:])
            print("Solution Generated: " + newInput[9:])
            return newInput