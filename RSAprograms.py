import math
import random
import time 

#to make sure number is prime 
def prime_numbers(n):
   if n<=1:
       return False
   if n==2:
       return True
   if n % 2 == 0 and n > 2:
       return False
   else:
       bound = math.sqrt(n) + 1
       for i in range(3, int(bound), 2):
           if n % i == 0:
               return False
       return True

#to generate random prime numbers for p and q
def generate_random_prime_number(bit_length = 8):

   while True:
       number = random.getrandbits(bit_length)
       if number % 2 != 0 and prime_numbers(number) and number.bit_length() == bit_length:
           return number

#generating random primes for p and q       
p=generate_random_prime_number(8)
q=generate_random_prime_number(8)

#ensuring that p and q are not the same number
while p == q:
    q = generate_random_prime_number(8)

#calculating n and totient
n=p*q
eul=(p-1)*(q-1)
e=3

#to calculate extended gcd   
start_time=time.time()    
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

#finds a suitable public exponent(e)
while e < eul:
    if extended_gcd(e, eul)[0] == 1:
        break
    else:
        e += 1

#factorising n to get p and q
def factorize(n):
    factors=[]
    d=2
    while n>1:
        while n%d==0:
            factors.append(d)
            n//=d
        d+=1
        if d*d>n:
            if n>1:
                factors.append(n)
            break
    return factors

#factorise n to obtain p and q
factors=factorize(n)
factorisedp=factors[1]
factorisedq=factors[0]

#calculating d (private key)
gcd, d, _ = extended_gcd(e, eul)

#calculating public and private key
public_key = {'n': n, 'e': e}
private_key = {'n': n, 'd': d}

#encrypting and decrypting m (message)
m= 11
C = pow(m, e, n)
M = pow(C, d, n)
end_time=time.time()
time=end_time-start_time

#print statements for results 
print(f"p is: {p} and q is: {q}")
print("n is: ", n, "\neul is: ", eul, "\ne is: ", e)
print(f"factorised p and q from modulus of n are: {factorisedp}, {factorisedq}")
print("Public Key:", public_key, "\nPrivate Key:", private_key)
print("\nEncrypted Message:", C, "\nDecrypted Message:", M)
print(f"Factorisation time: {time} seconds")


