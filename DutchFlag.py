#Dutch flag problem is a one-dimensional array that contains just three integers: [0, 1 and 2]
def dutch_flag(nums, pivot = 1):
    i = 0
    j = 1
    k = len(nums)-1
    

    while j <= k:
        if nums[j] < pivot:
            swap(nums, i, j)
            i = i + 1
            j = j + 1

        elif nums[j] > pivot:
            swap(nums, i, j)
            k = k -1

        else:
            j = j + 1
        

    return nums

def swap(nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]



print(dutch_flag([1, 0, 2, 0, 0, 0, 1, 1, 2, 2, 1, 2]))

