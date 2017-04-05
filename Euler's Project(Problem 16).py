number = 2**1000
onumber = number
sum_of_digits = 0
for i in str(onumber):
    remainder = number %10
    sum_of_digits = sum_of_digits + remainder
    number = number //10
print(sum_of_digits)
