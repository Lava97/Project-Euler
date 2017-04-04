sum = 0
fib= 0
n1 = 1
n2 = 0
even_num = []
while fib < 4000000:
    fib = n1 + n2
    n2 = n1
    n1 = fib
    if fib % 2 == 0:
        sum += fib
        even_num.append(fib)
print(even_num)
print(sum)
