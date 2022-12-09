# Python_Studies
1. TRAPPING RAIN WATER PROBLEM
Find the maximun height(MaxLeft) on the left and the maximum height (MaxRight) on the right. For each position, pick the mininum of the two heights and substract it by the height of the position. The answer is the capacity of that position.  Then move to the next position. The capacity of the area is the addition of all values.
If the number of bars is less than 3, then it can't trap any water. The first and last bars can't trap any water.


# Linked Lists
Used to store items efficiently
Need to know the index of array, very inmportant
Start with the head node, first one. Last node is null
Linked list need more memories than arrays, but there are no holes, so no need to shift all items, reducing the running time.
Node stores the given data

We can only access the head node, so always start from it
FAst when we manipulate the first item at 0(1) running time
Slow when we want to manipulate other items at 0(N) running time
Arrays are dynamic Data Structures, assume all items have different memories
Lists are static data structures, all items have the same memory allocation, we don't have random access
Running time depends on activities of the users, it's not predictable.
Predictability is an important feature of an application
