class Node: #first create a class for the node

    def __init__(self, data):
        self.data = data #storage of the data as linked list demands
        self.next_node = None #reference to the next node
                              #this is the node class
    def __repr__(self):
        return str(self.data)

       #Now create a class for the linked list itself

class LinkedList:    
    def __init__(self):
        self.head = None #this is the head node/ the first node of the LL                   
                         #We can access this node exclusively
        
        self.num_of_nodes = 0 #we need to store the num of nodes in the LL

    def insert_start(self, data): #insertion of nodes at the start
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None: #we need to check if node is empty
            self.head = new_node #then the item in new node becomes the first node
                                 #insertion at beginning is fast at 0(1) running time
        else: #this is when the LL is not empty
            new_node.next_node = self.head #we have to update the references
                                           #the new node becomes the first node and pointing 
                                           # to the previous head node
            
            self.head = new_node #the new node becomes the head node, ie. first item on list

    def insert_end(self, data): #insertion at the end
        self.num_of_nodes += 1 #increment one to each node
        new_node = Node(data) # the nodes in the node(data) function
       
        if self.head is None: #always check if it's empty
            self.head = new_node #inserted node automatically becomes first
        else:
            actual_node = self.head #create a var for the node to go to the end
                                    #and it's logically the head node cos that's all you can access
        while actual_node.next_node is not None: #as far as there is a value after a node
            actual_node = actual_node.next_node #the actual node is the last node
           
        actual_node.next_node = new_node   #the node to be inserted is the last one 
                                                

    def size_of_list(self): #a function to get the number of nodes
        return self.num_of_nodes 

    def traverse(self):
        actual_node = self.head #create a var for the node being inserted
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node


    def remove(self, data): #How to remove node from list
        if self.head is None:
            return 

        actual_node = self.head #store a reference to the actual node
                                #we have to track the previous node for future pointer updates, this is why doubly linked lists are better - we can get the previous node (here with linked lists it is impossible)
        previous_node = None #store a reference to the previous node

        while actual_node is not None and actual_node.data != data: #search for the item we want to remove
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return
        #update the references so we have the data we want to remove
        if previous_node is None: #makes reference to the head node, to   remove it
            self.head = actual_node.next_node 

        else:
            previous_node.next_node = actual_node.next_node
            #remove an internal node by updating the pointers
            #no need to del the node because the garbage collector will do that

    


linked_list = LinkedList()
linked_list.insert_start(10)
linked_list.insert_start("John")
linked_list.insert_start(7.5)
linked_list.insert_start("Mark")
linked_list.insert_start(34)
linked_list.insert_end(100)
linked_list.insert_end(1000)
linked_list.traverse()
print(454)
linked_list.remove("John")
linked_list.traverse()
        