def get_tidy_digits_left(num):
    
    last_digit = 0
    for i in range(len(num)):
        digit = int(num[i])

        if digit < last_digit:
            # Return the number of digits to the right of the current digit
            return len(num) - i

        last_digit = digit
    
    return 0
    
    
cases = int(input())

for i in range(cases):
    num = input()
    
    while num:
        digits_left = get_tidy_digits_left(num)
        
        if not digits_left:
            break
        
        num = str(int(num) - int(num[-digits_left:]) - 1)
        
    print("Case #{}: {}".format(i + 1, num))
