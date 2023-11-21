import os
from hashlib import sha256

def verify():
    #constructing file paths
    targetPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'target.txt')
    inputPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'input.txt')
    solutionPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'solution.txt')
    
    #reading file contents
    target = open(targetPath, 'r').read()
    input = open(inputPath, 'r').read()
    solution = open(solutionPath, 'r').read()
    
    #concatinate input and solution
    newInput = input + solution
    
    #calculate hash of newInput
    hex = sha256(newInput.encode()).hexdigest()
    
    #convert the hex hash to binary and make it 256 bits long
    binary = bin(int(hex, 16))[2:].zfill(256)
    
    if binary == target:
        print("1 - Solution is Valid")
    else:
        print("0 - Solution is Invalid")