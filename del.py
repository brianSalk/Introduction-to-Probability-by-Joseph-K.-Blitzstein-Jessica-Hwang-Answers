from math import e, factorial, perm
print(1/e)
num = factorial(26)
den = 0
for i in range(1,27):
    den += perm(26,i)
print(num/den)
