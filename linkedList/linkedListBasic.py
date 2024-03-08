
# Node class to create a node.
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next =None

# LinkedList class
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # Method to insert a node at the begining
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        else : 
            new_node.next = self.head
            self.head = new_node
            
    # Method to insert a node at specific index
    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == 0:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index ):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else: 
                print("Index not available")

    # Method to insert a node at the end 
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        
    # Methode to update a node
    def updateNode(self,val,index):
        current_node = self.head
        position = 0
        if position == index :
            current_node.data = val
        else :
            while(current_node != None and position+1 != index ):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
                
    # Method to delete node from begining
    def deleteNodeAtBegin (self):
        if(self.head == None):
            return
        self.head = self.head.next
        
    # Method to delete node at end
    def deleteNodeAtEnd(self):
        if(self.head == None):
            return
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None
        
    # Method to delete node at given index
    def deleteNodeAtindex(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.deleteNodeAtBegin()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
                
    # Method to delete a node by data
    def deleteNodebyData(self,data):
        current_node = self.head
        # Check if the head node contains the specified data
        if current_node.data == data:
            self.deleteNodeAtBegin()
            return
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next
    
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next
            
    # Method to traverse a linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    # Method to find size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
        
