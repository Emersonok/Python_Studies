# Python_Studies
1. TRAPPING RAIN WATER PROBLEM
Find the maximun height(MaxLeft) on the left and the maximum height (MaxRight) on the right. For each position, pick the mininum of the two heights and substract it by the height of the position. The answer is the capacity of that position.  Then move to the next position. The capacity of the area is the addition of all values.
If the number of bars is less than 3, then it can't trap any water. The first and last bars can't trap any water.


# Linked Lists
Steps:
1- create Node Class with a func that contains data and next node variables
2- Another func to return data as string
3- Next create Linked List Class that contains a func of the head node (self.head) and number of nodes variables
Create insertion, Steps
Insertion at start is 0(N) running time
1- Count num of nodes as += 1
2- Create a variable to contain the data (newNode = Node(data)
3- If head is none, then self.head = newnode
4- Else, newnode + nextnode = self.head
5- update references (self.head = newnode)

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
Linked Lists need more memory than arrays
Advantage is there can't be holes, no need shifting items as done in arrays.
Node stores data itself and a reference to the next node, the last node points to NULL
We can only access the head node, to access other items of the Linked list, we need to start from the head node and follow the references until we find the node we're looking for
We are not able to get the previous node, can only get the next node, so you have to store a reference to the previous node

# Data Structures
Everything needs to be created, unless it exists internally
Create functions for each activity
First algorithm should return 0 if list is empty or = 0


