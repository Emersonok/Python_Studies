class Stack:  #creation of stack
    def __init__(self): 
        self.stack = [] #stack is a one-dimensional array

#insert item into the stack(push)
    def push(self, data):
        self.stack.append(data) #append adds a new item

#remove item from the stack(pop)
    def pop(self):
        if self.stack_size() < 1:
            return -1
        data = self.stack[-1] #to access the last data 
        del self.stack[-1] #to remove the last item
        return data

#return the last item without removing it(peek)
    def peek(self):
        return self.stack[-1]

    def is_empty(self): #return this function if array is empty
        return self.stack == [] #will return True or False

    #to get the size of the array
    def stack_size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
   
print(stack.pop())  
print("Size is %d" % stack.stack_size()) 
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.stack_size())