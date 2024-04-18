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
