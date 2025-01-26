#How do you merge two sorted linked lists?

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy node to simplify the merge process
    dummy = ListNode()
    current = dummy
    
    # Traverse through both lists
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # If one list is exhausted, append the remaining elements of the other list
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next

#example
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Example usage
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 4])

merged_list = mergeTwoLists(l1, l2)
print_linked_list(merged_list)
