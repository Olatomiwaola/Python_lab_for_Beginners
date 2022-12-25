check = 9 %5
print(check)
def prime_numbers(listing):

    primes = list()
    flag = False
    for i in listing:
        for c in range(2, i):
            print(c)
            if c%i == 0 :
                continue
            else: 
                primes.append(i)
                
    return primes
    
print(prime_numbers([2,3,4,5]))

        
                    
                    
                
    