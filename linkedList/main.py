from linkedListBasic import LinkedList

# create a new linked list
llist = LinkedList()
 
# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data")
llist.printLL()
 
# remove a nodes from the linked list
print("\nRemove First Node")
llist.deleteNodeAtBegin()
print("Remove Last Node")
llist.deleteNodeAtEnd()
print("Remove Node at Index 1")
llist.deleteNodeAtindex(1)
 
 
# print the linked list again
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()
 
print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL()) 