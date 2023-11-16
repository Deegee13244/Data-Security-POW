import os
from hashlib import sha256

def verify():
    targetPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'target.txt')
    inputPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'input.txt')
    solutionPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'solution.txt')
    
    target = open(targetPath, 'r').read()
    input = open(inputPath, 'r').read()
    solution = open(solutionPath, 'r').read()
    
    newInput = input + solution
    hex = sha256(newInput.encode()).hexdigest()
    binary = bin(int(hex, 16))[2:].zfill(256)
    
    if binary <= target:
        print("1 - Solution is Valid")
    else:
        print("0 - Solution is Invalid")