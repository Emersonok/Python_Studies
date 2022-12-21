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


    def mid_node(self): #create two pointers to run side by side
        fast_pointer = self.head #first pointer runs two times 
        slow_pointer = self.head #second pointer runs only once

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

linked_list = LinkedList()
linked_list.insert_start(20)
linked_list.insert_start(38)
linked_list.insert_start(19)

print(linked_list.mid_node().data)

        

        
