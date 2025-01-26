#How do you print a binary tree in vertical order?

#Approach : We will use a queue to perform a level-order traversal. 
#Each element in the queue will store the node and its corresponding horizontal distance (HD) from the root.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def vertical_order(root):
    if not root:
        return

    # Dictionary to store the vertical order traversal
    vertical_dict = {}

    # Queue to store nodes along with their horizontal distance
    queue = [(root, 0)]

    while queue:
        node, hd = queue.pop(0)

        if hd in vertical_dict:
            vertical_dict[hd].append(node.key)
        else:
            vertical_dict[hd] = [node.key]

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    for key in sorted(vertical_dict):
        for value in vertical_dict[key]:
            print(value, end=' ')
        print()

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

vertical_order(root)