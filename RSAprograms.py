import math
import random
import time 
# from keygeneration import keygeneration

#getting p and q values
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

start_time = time.perf_counter()
n = p * q
eul = (p - 1) * (q - 1)
e = 3
#to calculate extended gcd     
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


#finds a suitable public exponent(e)
def public_exponent(e,eul):
    while e < eul:
        if extended_gcd(e, eul)[0] == 1:
            break
        else:
            e += 1
    return e

e=public_exponent(e,eul)
#calculating d (private key)
gcd, d, _ = extended_gcd(e, eul)
def calculate_d(e, phi):
    _, d, _ = extended_gcd(e, phi)
    return d % eul

# Assuming e and phi are already calculated
d = calculate_d(e, eul)
d = d % eul  # Ensure d is positive

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

# #getting p and q values
# p = int(input("Enter the value of p: "))
# q = int(input("Enter the value of q: "))

# start_time = time.perf_counter()

# n = p * q
# eul = (p - 1) * (q - 1)
# e = 3
# e=public_exponent(e,eul)
# #calculating d (private key)
# gcd, d, _ = extended_gcd(e, eul)
# d = d % eul  # Ensure d is positive

#factorise n to obtain p and q
factors=factorize(n)
factorisedp=factors[1]
factorisedq=factors[0]


#calculating public and private key
public_key = {'n': n, 'e': e}
private_key = {'n': n, 'd': d}

#encrypting and decrypting m (message)
m= 11
C = pow(m, e, n)
M = pow(C, d, n)
end_time = time.perf_counter()
time_taken = (end_time - start_time) * 1000  # Convert to milliseconds

#print statements for results 
print("factorisation results: ")
print(f"p is: {p} and q is: {q}")
print("n is: ", n, "\neul is: ", eul, "\ne is: ", e)
print(f"factorised p and q from modulus of n are: {factorisedp}, {factorisedq}")
print("Public Key:", public_key, "\nPrivate Key:", private_key)
print("\nEncrypted Message:", C, "\nDecrypted Message:", M)
print(f"Factorisation time: {time_taken:.6f} seconds")


