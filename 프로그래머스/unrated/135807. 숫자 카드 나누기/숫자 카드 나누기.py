import math
def solution(arrayA, arrayB):
    answer = 0
    
    def findGCD(array):
        gcd = 0
        for i in range(len(array)):
            gcd = math.gcd(gcd, array[i])
        return gcd
    
    def checkGCD(array, gcd):
        for i in range(len(array)):
            if array[i] % gcd == 0:
                return 0
            
        return gcd
    
    gcdA, gcdB = findGCD(arrayA), findGCD(arrayB)
    gcdA, gcdB = checkGCD(arrayB, gcdA), checkGCD(arrayA, gcdB)
    
    if gcdA == 0 and gcdB == 0:
        return 0
    
    return max(gcdA, gcdB)