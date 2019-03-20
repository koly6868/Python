from math import sqrt, inf
import random as r

def max(a,b):
    if b > a:
        return b
    else:
        return a


# Generate Fibonachi sequence
def Fibonachi(count):
    assert count > 1, 'count must be more than 1'
    numbers = []
    a = 1
    b = 1
    c = 0
    numbers.append(a)
    numbers.append(b)
    for i in range(2, count):
        c = a + b
        numbers.append(c)
        a = b
        b = c 
    
    return numbers


# Find simple multiplaers and count of them
def SimpleMultiplaers(number):
    val = number
    multiplaers = {}
    mult = 2
    while val >= mult:
        if val % mult == 0:
            multiplaers[mult] = 0
            while val % mult == 0:
                multiplaers[mult] += 1
                val = int(val / mult)
        mult += 1
           
    return multiplaers


# optimazed algoritm for getting simple number for 1 to limit
def SimpleNumbers(limit = -1):
    strm = []
    if limit == -1:
        limit = int(inf)
    number = 1
    
    while number < limit:
        i = 3
        maxMult = int(sqrt(number))
        while i <= maxMult:
            if number % i == 0:
                break
            i += 2
        else:
            strm.append(number)
        
        number += 2
    return strm


# Evklid
def NOD(first,second):
    a = first
    b = second
    if a == b:
        return a
    
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    
    return a + b


# Ferma check (probablistick)
def IsSimple(number):
    val = number
    r.seed()
    p = r.randint(val, 2*val)
    if (val ** p) % p == val % p:
        return True
    else:
         return False
    