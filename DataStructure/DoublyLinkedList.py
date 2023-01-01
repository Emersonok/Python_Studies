class Node:

    def __init__(self, data):
        self.data = data #data contained in linked list
        self.next = None # next item to be inserted
        self.previous = None #previous item


class DoublyLinkedList:

    def __init__(self):
        self.head = None #First node of the list
        self.tail = None #last node/item of the list

    

    def insert(self, data): #to insert at the end of linked list, to manipulate the tail node
        new_node = Node(data) #the item to be inserted is called new node

        if self.head is None: #do this when list is empty
            self.head = new_node #the item inserted is first at same time the last
            self.tail = new_node

        else: #do this when list isn't empty
            new_node.previous = self.tail
            self.tail.next = new_node #when list isn't empty, the inserted item should appear at the tail, end
            self.tail = new_node #update the tail to be the new node

    def traverse_backward(self): #to loop through items from the back
        actual_node = self.tail #give another name to the tail node to be used in the loop

        while actual_node is not None: #while tail isn't equal to zero or isn't empty
            print("%d" % actual_node.data ) # %d referes to the data to be typed by user
            actual_node = actual_node.previous

    def traverse_forward(self): #to loop through items from the front
        actual_node = self.head #give another name to the tail node to be used in the loop

        while actual_node is not None: #while tail isn't equal to zero or isn't empty
            print("%d" % actual_node.data ) # %d referes to the data to be typed by user
            actual_node = actual_node.next

linked_list = DoublyLinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)


linked_list.traverse_backward()
linked_list.traverse_forward()

        