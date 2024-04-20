import math
import random
import time

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 and n > 2:
        return False
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True

# Function to generate a random prime number with specified bit length
def generate_random_prime_number(bit_length):
    while True:
        number = random.getrandbits(bit_length)
        if number % 2 != 0 and is_prime(number) and number.bit_length() == bit_length:
            return number

# Function to factorise n to obtain p and q
def factorise(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

# Main function for factorisation
def factorisation(p, q):
    n = p * q
    eul = (p - 1) * (q - 1)
    e = 3
    e = public_exponent(e, eul)
    gcd, d, _ = extended_gcd(e, eul)
    d = d % eul  # Ensure d is positive
    factors = factorise(n)
    factorisedp = factors[1]
    factorisedq = factors[0]
    public_key = {'n': n, 'e': e}
    private_key = {'n': n, 'd': d}
    m = 11
    C = pow(m, e, n)
    M = pow(C, d, n)
    return n, eul, e, factorisedp, factorisedq, public_key, private_key, C, M

# Main function for brute force attack
def brute_force(p, q):
    n = p * q
    eul = (p - 1) * (q - 1)
    e = 3
    m = 11
    public_e = public_exponent(e, eul)
    C = pow(m, e, n)
    d = 2
    attempts = 0
    while True:
        if pow(C, d, n) == m:
            break
        attempts += 1
        d += 1
    d = d % eul  # Ensure d is positive
    M = pow(C, d, n)
    public_key = {'n': n, 'e': e}
    private_key = {'n': n, 'd': d}
    return n, eul, e, public_key, private_key, C, M, attempts

# Function to calculate extended gcd
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Function to find a suitable public exponent (e)
def public_exponent(e, eul):
    while e < eul:
        if extended_gcd(e, eul)[0] == 1:
            break
        else:
            e += 1
    return e

# Get user input for bit length
bit_length = int(input("Enter the bit length for generating prime numbers: "))
p = generate_random_prime_number(bit_length)
q = generate_random_prime_number(bit_length)

# Perform factorisation
n_factorisation, eul_factorisation, e_factorisation, factorisedp, factorisedq, public_key_factorisation, private_key_factorisation, C_factorisation, M_factorisation = factorisation(p, q)

# Perform brute force attack
n_bruteforce, eul_bruteforce, e_bruteforce, public_key_bruteforce, private_key_bruteforce, C_bruteforce, M_bruteforce, attempts_bruteforce = brute_force(p, q)

# Print the results
print("Factorisation results:")
print(f"p is: {p} and q is: {q}")
print("n is: ", n_factorisation, "\neul is: ", eul_factorisation, "\ne is: ", e_factorisation)
print(f"factorised p and q from modulus of n are: {factorisedp}, {factorisedq}")
print("Public Key:", public_key_factorisation, "\nPrivate Key:", private_key_factorisation)
print("\nEncrypted Message:", C_factorisation, "\nDecrypted Message:", M_factorisation)

print("Brute force attack results:")
print(f"p is: {p} and q is: {q}, message is: {M_bruteforce}")
print(f"Brute force attack succeeded after {attempts_bruteforce} attempts! Private exponent d is: {private_key_bruteforce['d']}")