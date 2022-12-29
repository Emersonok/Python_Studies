class Max_Stack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)

        #if there's only one value in the main stack, repeat it in the max stack
        if (len(self.main_stack)==1):
            self.max_stack.append(data)
            return
        #check if the inserted data is greater than the last data on max stack, if yes, append
        if data > self.max_stack[-1]:
            self.max_stack.append(data)

        else: #if it's not greater, append the last item
            self.max_stack.append(self.max_stack[-1])



    def pop(self):
        self.max_stack.pop()
        return self.max_stack.pop()

    def get_max(self):
        return self.max_stack.pop()



stack = Max_Stack()
stack.push(1)
stack.push(2)
stack.push(30)
stack.push(40)
stack.push(10)
print(stack.get_max())

        