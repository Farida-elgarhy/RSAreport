import math
import random


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
def generate_random_prime_number(bit_length):
   while True:
       number = random.getrandbits(bit_length)
       if number % 2 != 0 and prime_numbers(number) and number.bit_length() == bit_length:
           return number
       
# #to calculate extended gcd     
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# #finds a suitable public exponent(e)
def public_exponent(e,eul):
    while e < eul:
        if extended_gcd(e, eul)[0] == 1:
            break
        else:
            e += 1
    return e

def keygeneration(bit_length):     
    if bit_length==8 or bit_length==16: 
        #generating random prime numbers for p and q
        p=generate_random_prime_number(bit_length)
        q=generate_random_prime_number(bit_length)
        #ensuring that p and q are not the same number
        while p == q:
            q = generate_random_prime_number(bit_length)
        return p,q
    else: 
        print("bit length has to be 8 or 16, try again")
        return None, None
bit_length=int(input("enter bit length 8 or 16 "))
p,q=keygeneration(bit_length)

if p and q:
    n = p * q
    eul = (p - 1) * (q - 1)
    e = 3
    e=public_exponent(e,eul)

    #calculating d (private key)
    gcd, d, _ = extended_gcd(e, eul)
    d = d % eul  # Ensure d is positive


    print(f"{bit_length} bit p is: ", p)
    print(f"{bit_length} bit q is: ", q)
    print(f"n is: {n}")
    print(f"eul is: {eul}")
    print(f"e is: {e}")
    print(f"private exponent (d) is: {d}")
