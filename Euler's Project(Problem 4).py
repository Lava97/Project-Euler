def makePalindrome(number):
    digit = 0
    reverse = ""
    onumber = number
    flag = 0
    while(number > 0):
        remainder = number %10    
        reverse = reverse + str(remainder)
        number = number //10
    return int(str(onumber) + str(reverse))

not_finished = True
number = 997
i = 999
while(not_finished):
    i = 999
    palindrome = makePalindrome(number)
    while(i > 99):
        if ((palindrome / i > 999) or i*i < palindrome):
            break
        
        if(palindrome % i == 0):
            not_finished = False
            factor1 = i
            factor2 = palindrome /i
            break
        i = i - 1
    number = number - 1
print("The palindrome",palindrome,"and it's factors are:",factor1,factor2,".")
