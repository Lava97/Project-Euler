L = [i**2 for i in range(1,101)]
sum_of_squares = 0
square_of_sum = 0
for j in range(len(L)):
    sum_of_squares = sum_of_squares + L[j]
M = [m for m in range(1,101)]
for n in range(len(M)):
    square_of_sum = square_of_sum + M[n]
square_of_sum = square_of_sum ** 2
difference = square_of_sum - sum_of_squares
print(difference)
