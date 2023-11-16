import os

def targetGen(d):
    targetPath = os.path.join(os.path.dirname(__file__), '..', 'data', 'target.txt')
    
    target = int(d)*'0'+(256-int(d))*'1'
    print("Target Generated: " + target)
    open(targetPath, "w").write(target)
    