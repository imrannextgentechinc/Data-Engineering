#How do you remove a loop in a linked list?

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_and_remove_loop(head):
    slow = head
    fast = head

    # Detect loop using Floyd’s Cycle-Finding Algorithm
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast meet at some point then there is a loop
        if slow == fast:
            remove_loop(slow, head)
            return

def remove_loop(loop_node, head):
    ptr1 = head
    while True:
        ptr2 = loop_node
        while ptr2.next != loop_node and ptr2.next != ptr1:
            ptr2 = ptr2.next

        if ptr2.next == ptr1:
            break

        ptr1 = ptr1.next

    ptr2.next = None

# Example usage:
# Creating a looped linked list for testing
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next.next  # Creating a loop

detect_and_remove_loop(head)

# Print the list after removing the loop
current = head
while current:
    print(current.value, end=' ')
    current = current.next
# Output: 1 2 3 4 5
# The loop has been removed from the linked list
# The list is now 1 -> 2 -> 3 -> 4 -> 5 -> None


# Time complexity: O(n)
# Space complexity: O(1)
# The detect_and_remove_loop function has a time complexity of O(n) and a space complexity of O(1).


#explanation
# To remove a loop in a linked list, we can use Floyd’s Cycle-Finding Algorithm to detect the loop in the linked list.
# Once the loop is detected, we can find the starting point of the loop and remove it by breaking the loop at that point.
# The detect_and_remove_loop function takes the head of the linked list as input and uses two pointers, slow and fast, to detect the loop.
# If a loop is found, the remove_loop function is called to remove the loop by breaking the link at the starting point of the loop.
# The remove_loop function takes the loop node and the head of the linked list as input and iterates through the linked list to find the starting point of the loop.
# Once the starting point is found, the link is broken, and the loop is removed from the linked list.
# Finally, the list is printed after removing the loop.