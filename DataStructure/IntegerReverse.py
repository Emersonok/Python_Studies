def integer_reverse(num):
    reversed_num = 0
    

    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num = num // 10 # // is an integer division
    return reversed_num


print(integer_reverse(2345))
    



        