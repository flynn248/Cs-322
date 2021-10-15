# Developed by Shane Flynn
# List all prime numbers including and below a given integer

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

def main():
    print(listPrimesBelow(2))
    print(listPrimesBelow(13))
    print(listPrimesBelow(52))
    print(listPrimesBelow(102))
    print(listPrimesBelow(107))

if __name__ == '__main__':
    main()