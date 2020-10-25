def is_prime(num):
    isPrime = True

    if(num == 1):
        return True
    
    #print(range(2,(num//2)+1))

    for i in range(2,num//2+1):
        if (num % i) == 0:
            isPrime = False
            break

    if(isPrime):
        print(num)

    return isPrime

print(is_prime(7))

def getFactorial(num):
    
    facto = 1

    for i in range(1, num):
        facto = facto * i

    return facto

print(getFactorial(4))

l = [getFactorial(X) for X in range(1, 100) if is_prime(X) == True]

print(l)

# for prime
# from 1 to floor of root n