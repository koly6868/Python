def max(a,b):
    if b > a:
        return b
    else:
        return a



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