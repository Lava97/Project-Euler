import math
def is_prime(num):
    if (num > 1):
       for i in range(3,int(round(math.sqrt(num)+1)),2):
           if (num % i) == 0:
               return False
               break
       else:
           return True
           
    else:
       return False

summation = 2
for j in range(3,2000000):
    if(j%2==0):
        continue
    print(j)
    bool_val = is_prime(j)
    if (bool_val == True):
        summation = summation + j
print(summation)


