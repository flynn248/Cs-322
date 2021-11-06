# Developed by Shane Flynn
# List all prime numbers including and below a given integer
# isBst: Check if a list is a valid binary tree

from io import RawIOBase


def checkIfPrime(i: int, x: int=2) -> bool:
    if (i % x) == 0:
        return False
    elif x == int(i / 2):
        return True
    else:
        return checkIfPrime(i, x + 1)

def buildPrimeList(primeList: list, isPrime: bool, n: int, i: int) -> list:
    if i == 2:
        return [2]
    elif i == 3:
        return [2,3]
    
    isPrime = checkIfPrime(i)

    if isPrime:
        primeList = buildPrimeList(primeList, True, n, i - 1)
        primeList.append(i)
        return primeList
    else:
        primeList = buildPrimeList(primeList, True, n, i - 1)
        return primeList


def listPrimesBelow(n: int) -> list:
    if n == 0 or n == 1 or n == 2:
        return []
    
    return buildPrimeList([], True, n - 1, n - 1)

def isBst(binT: list) -> bool:
    if not binT: # if list is empty
        return True

    if not binT[1] and not binT[2]: # if left and right children don't exist
        return True
    
    parentValue = binT[0]
    isValid = True

    for i in range(1, 3):
        if binT[i]:
            childValue = binT[i][0]
            if i % 2 == 1: # left child node
                if childValue > parentValue:
                    isValid = False
            else: # right child node
                if childValue <= parentValue:
                    isValid = False
            
            if isValid:
                isValid = isBst(binT[i])
    
    return isValid


def isValid(binT: list, i: int) -> bool:
    parentValue = binT[0]
    childValue = binT[i][0]
    if i % 2 == 1: # left child node
        if childValue > parentValue:
            return False
    else: # right child node
        if childValue <= parentValue:
            return False
# make a helper function

def main():
    
    print(f"Primes below 2:\n{listPrimesBelow(2)}\n")
    print(f"Primes below 13:\n{listPrimesBelow(13)}\n")
    print(f"Primes below 52:\n{listPrimesBelow(52)}\n")
    print(f"Primes below 102:\n{listPrimesBelow(102)}\n")
    print(f"Primes below 107:\n{listPrimesBelow(107)}\n")

    tests = [
    [4, [2, [1, [], []], [3, [], []]], [6, [5, [], []], []]], #t
    [4, [2, [1, [], []], [3, [], []]], [6, [9, [], []], []]], #f
    [4, [2, [1, [], []], [3, [], []]], [1, [5, [], []], []]], #f
    [4, [7, [1, [], []], [3, [], []]], [6, [5, [], []], []]], #f
    [4, [2, [1, [], []], [1, [], []]], [6, [5, [], []], []]], #f
    [4, [2, [4, [], []], [3, [], []]], [6, [5, [], []], []]]] #f

    for i in range(0, len(tests)):
        print(isBst(tests[i]))

if __name__ == '__main__':
    main()



'''
    if not binT[1]: # if left sub-tree doesn't exist
        lRetVal = True
    else:
        lChildValue = binT[1][0]
        
        if lChildValue <= parentValue:
            lRetVal = isBst(binT[1])
        else:
            lRetVal = False
    
    rRetVal = False

    if not binT[2]: # if right sub-tree doesn't exist
        rRetVal = True
    else:
        rChildValue = binT[2][0]

        if rChildValue > parentValue:
            rRetVal = isBst(binT[2])
        else:
            rRetVal = False
    
    if lRetVal and rRetVal:
        return True
    else:
        return False
'''