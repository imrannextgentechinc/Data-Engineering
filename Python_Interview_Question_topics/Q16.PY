#How do you find the middle element of a linked list?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5

linkedList = Node(1)
linkedList.next = Node(2)
linkedList.next.next = Node(3)
linkedList.next.next.next = Node(4)
linkedList.next.next.next.next = Node(5)

print("The middle element is:", find_middle(linkedList))


#explaination
#The idea is to use two pointers, slow_ptr and fast_ptr. 
# The slow_ptr moves one node at a time while the fast_ptr moves two nodes at a time. 
# When the fast_ptr reaches the end of the list, the slow_ptr will be at the middle element. 
# This approach has a time complexity of O(n) where n is the number of nodes in the linked list.
# In the example usage, the linked list is created with elements 1, 2, 3, 4, and 5. 
# The middle element is found using the find_middle function, which returns the data of the middle node (in this case, 3). 
# The output is printed as "The middle element is: 3".
