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

start = time.perf_counter()
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
start_time=time.perf_counter()  
# Brute force attack to find the private exponent d
def brutedecrypt(e, n, C):
    start_time = time.time()
    attempts = 0
    d = 1
    decrypted_message = ""
    while True:
        if pow(C,d, n) == m:
            break
        d += 1
        attempts += 1
    end_time = time.time()
    brute_force_time = end_time - start_time
    return d, attempts, brute_force_time

d, attempts, brute_force_time = brutedecrypt(e, n, C)
#D=pow(e,-1,eul)
public_key = {'n': n, 'e': e}
private_key = {'n': n, 'd': d}
#encrypting and decrypting m (message)
m= 11
C = pow(m, e, n)
end_time = time.perf_counter()
time_taken = (end_time - start_time) * 1000  # Convert to milliseconds

# Print the results

print(f"Brute force attack succeeded after {attempts} attempts! Private exponent d is: {d}")
print(f"Brute force attack took: {time_taken} seconds")