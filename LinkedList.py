class Node: #first create a class for the node

    def __init__(self, data):
        self.data = data #storage of the data as linked list demands
        self.next_node = None #reference to the next node
                              #this is the node class


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
            actual_node = new_node   #the node to be inserted is the last one 
                                                

    def size_of_list(self): #a function to get the number of nodes
        return self.num_of_nodes
        