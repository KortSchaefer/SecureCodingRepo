isPrime = input("Enter a number to check if it is prime: ")
isPrime = int(isPrime)

primes = []
def check_prime(isPrime):
    count = 0
    factors = []
    
    for i in range(1, isPrime + 1):
        if isPrime % i == 0:
            count+=1
            factors+= [i]
            
    if count <= 2:
        primes.append(isPrime)
    
        
    
    print(primes)
for i in range(1, isPrime + 1):
    check_prime(i)
