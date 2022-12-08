#How to reverse the items on a list

def reverse (nums):    #create the function name reverse
    start = 0        # first item of the list
    end = len(nums)-1 # last item of the list

    while end > start: #as far as values of last position is ahead of that at start positon
        nums[start], nums[end] = nums[end], nums[start] # the end position should become start position
        start = start + 1
        end = end - 1

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse(n)
print(n)


    