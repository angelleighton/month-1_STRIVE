#Prime number EX 5.6
def prime(max_numb):
    primes = []
    for possiblePrime in range(2, max_numb+1):
        
        isPrime = True
        for i in range(2, possiblePrime):
            if possiblePrime % i == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(possiblePrime)
    print(primes)


prime(9999)