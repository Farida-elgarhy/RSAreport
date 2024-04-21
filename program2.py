import math
import random
import time 
from RSAprograms import public_exponent

# getting p and q
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

start_time = time.perf_counter()

# calculating n and totient
n = p * q
eul = (p - 1) * (q - 1)
e = 3

# encrypting m (message)
m = 11
public_e = public_exponent(e, eul)
C = pow(m, e, n)