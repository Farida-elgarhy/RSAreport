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

print(f"p is: {p} and q is: {q}")
print("n is: ", n, "\neul is: ", eul, "\ne is: ", e)
