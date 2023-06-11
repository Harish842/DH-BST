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
                    parent.leftis = None
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

class DatabaseIndex:
    def __init__(self, size):
        self.index = DH_BST(size)

    def insert(self, key, value):
        self.index.insert(key, value)

    def search(self, key):
        return self.index.search(key)

    def delete(self, key):
        self.index.delete(key)

# Create a database index with a size of 10
database_index = DatabaseIndex(10)

# Insert key-value pairs into the index
database_index.insert(5, "Value 1")
database_index.insert(10, "Value 2")
database_index.insert(3, "Value 3")
database_index.insert(7, "Value 4")
database_index.insert(2, "Value 5")

# Search for a key in the index
search_result = database_index.search(10)
if search_result is not None:
    print(search_result)  # Output: "Value 2"
else:
    print("Key not found")

search_result = database_index.search(15)
if search_result is not None:
    print(search_result)
else:
    print("Key not found")  # Output: "Key not found"

# Delete a key from the index
database_index.delete(3)

# Search for the deleted key
search_result = database_index.search(3)
if search_result is not None:
    print(search_result)
else:
    print("Key not found")  # Output: "Key not found"
