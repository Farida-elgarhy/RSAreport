import math
import random
import time 
from RSAprograms import public_exponent

#to make sure number is prime 
def prime_numbers(n):
   if n<=1:
       return False
   if n==2:
       return True
   if n % 2 == 0 and n > 2:
       return False
   else:
       for i in range(3, int(math.sqrt(n) + 1), 2):
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

#encrypting m (message)
m= 11
public_e=public_exponent(e,eul)
C = pow(m, e, n)

# Brute force attack to find the private exponent d
start_time = time.perf_counter()
# def brutedecrypt(e, n, C,m):
#     attempts = 0
#     d = 1
#     while True:
#         M = pow(C, d, n)
#         if M == m:
#             break
#         d += 1
#         attempts += 1
#     return d, attempts
def brutedecrypt(e, n, C):
    d = 2
    attempts=0
    while True:
        if pow(C, d, n) == m:
            return d, attempts
        attempts+=1
        d += 1

d, attempts= brutedecrypt(e,n,C)
d = d % eul  # Ensure d is positive
M = pow(C, d, n)
public_key = {'n': n, 'e': e}
private_key = {'n': n, 'd': d}


end_time = time.perf_counter()
time_taken = (end_time - start_time) * 1000  # Convert to milliseconds

# Print the results
print(f"p is: {p} and q is: {q}, message is: {M}")
print(f"Brute force attack succeeded after {attempts} attempts! Private exponent d is: {d}")
print(f"Brute force attack took: {time_taken:.6f} seconds")