import time

class DHBSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class DHBST:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if not self.root:
            self.root = DHBSTNode(key, value)
        else:
            self._insert_node(self.root, key, value)
    
    def _insert_node(self, node, key, value):
        if key < node.key:
            if node.left:
                self._insert_node(node.left, key, value)
            else:
                node.left = DHBSTNode(key, value)
        elif key > node.key:
            if node.right:
                self._insert_node(node.right, key, value)
            else:
                node.right = DHBSTNode(key, value)
        else:
            node.value = value
    
    def search(self, key):
        return self._search_node(self.root, key)
    
    def _search_node(self, node, key):
        if not node or node.key == key:
            return node.value
        elif key < node.key:
            return self._search_node(node.left, key)
        else:
            return self._search_node(node.right, key)

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node has two children
            min_node = self._find_min_node(node.right)
            node.key = min_node.key
            node.value = min_node.value
            node.right = self._delete_node(node.right, min_node.key)

        return node

    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


class FileMetadata:
    def __init__(self, name, size, permissions):
        self.name = name
        self.size = size
        self.permissions = permissions

file_metadata = [
    FileMetadata("file1.txt", 1024, "rw"),
    FileMetadata("file2.txt", 2048, "r"),
    FileMetadata("file3.txt", 512, "rwx"),
    # Additional file metadata...
]

file_index = DHBST()
for metadata in file_metadata:
    file_index.insert(metadata.name, metadata)

# Example usage:
file_name = "file2.txt"
found_file = file_index.search(file_name)
if found_file:
    print(f"File found: {found_file.name}, Size: {found_file.size}, Permissions: {found_file.permissions}")
else:
    print("File not found")
