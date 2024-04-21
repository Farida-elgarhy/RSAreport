import math
import time 

# getting p and q values
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
e = int(input("enter e: "))




# calculating n and totient
n = p * q
eul = (p - 1) * (q - 1)

# encrypting m (message)
m = 11
C = pow(m, e, n)

# Brute force attack to find the private exponent d
def brutedecrypt(e, n, C):
    d = 1
    attempts = 0
    while True:
        if pow(C, d, n) == m:
            break
        attempts += 1
        d += 1
    return d, attempts

start_time = time.perf_counter()
d, attempts = brutedecrypt(e, n, C)
d = d % eul  # Ensure d is positive
end_time = time.perf_counter()
#decrypting the message (m)
M = pow(C, d, n)

# time calculation
time_taken = (end_time - start_time) * 1000  # Convert to milliseconds

#calculating public and private key
public_key = {'n': n, 'e': e}
private_key = {'n': n, 'd': d}

# Print the results
print("brute force results: ")
print(f"p is: {p} and q is: {q}, message is: {M}")
print(f"Brute force attack succeeded after {attempts} attempts! Private exponent d is: {d}")
print(f"Brute force attack took: {time_taken:.6f} milliseconds")
