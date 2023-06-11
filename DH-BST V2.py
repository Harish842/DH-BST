# Define the DH_BST class and its methods

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class DH_BST:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        index = self.hash_func1(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            node = self.table[index]
            while True:
                if key == node.key:
                    node.value = value
                    break
                elif key < node.key:
                    if node.left is None:
                        node.left = Node(key, value)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(key, value)
                        break
                    node = node.right

    def search(self, key):
        index = self.hash_func1(key)

        if self.table[index] is None:
            return None
        else:
            node = self.table[index]
            while node is not None:
                if node.key == key:
                    return node.value
                elif key < node.key:
                    node = node.left
                else:
                    node = node.right

            return None

    def delete(self, key):
        index = self.hash_func1(key)

        if self.table[index] is None:
            return
        else:
            root = self.table[index]
            parent = None
            node = root

            while node is not None and node.key != key:
                parent = node
                if key < node.key:
                    node = node.left
                else:
                    node = node.right

            if node is None:
                return

            if node.left is None and node.right is None:
                if parent is None:
                    self.table[index] = None
                elif parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

            elif node.left is not None and node.right is None:
                if parent is None:
                    self.table[index] = node.left
                elif parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left

            elif node.left is None and node.right is not None:
                if parent is None:
                    self.table[index] = node.right
                elif parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right

            else:
                successor_parent = node
                successor = node.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right

                node.key = successor.key
                node.value = successor.value

    def hash_func1(self, key):
        return hash(key) % self.size

    def hash_func2(self, key):
        return 1 + (hash(key) % (self.size - 1))


# Use the DH_BST class to insert, search, and delete nodes

bst = DH_BST(10)

bst.insert("apple", 1)
bst.insert("banana", 2)
bst.insert("cherry", 3)
bst.insert("date", 4)

print(bst.search("cherry"))  # Output: 3

bst.delete("banana")
print(bst.search("banana"))  # Output: None