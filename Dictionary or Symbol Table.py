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
            if node:
                return node.value
            else:
                return None
        elif key < node.key:
            return self._search_node(node.left, key)
        else:
            return self._search_node(node.right, key)


# Example usage:
dh_bst = DHBST()
dh_bst.insert(5, "Value 1")
dh_bst.insert(10, "Value 2")
dh_bst.insert(3, "Value 3")

search_result = dh_bst.search(10)
if search_result is not None:
    print(search_result)  # Output: "Value 2"
else:
    print("Key not found")

search_result = dh_bst.search(15)
if search_result is not None:
    print(search_result)
else:
    print("Key not found")  # Output: "Key not found"
