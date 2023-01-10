

input_zero = False
while not input_zero:
    num = int(input("Write a number:\n"))
    if num == 0 or num == 23:
        input_zero = True
        print("Process Finalized")
