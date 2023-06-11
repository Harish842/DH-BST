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
            return node
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


class CachedData:
    def __init__(self, data):
        self.data = data
        self.timestamp = time.time()  # Store timestamp for cache expiration

cache = DHBST()

def get_data_from_cache(key):
    cached_node = cache.search(key)
    if cached_node:
        cached_data = cached_node.value
        if time.time() - cached_data.timestamp <= CACHE_EXPIRY_TIME:
            return cached_data.data
        else:
            cache.delete(key)  # Remove expired cache
    return None

def add_data_to_cache(key, data):
    cache.insert(key, CachedData(data))

# Example usage:
CACHE_EXPIRY_TIME = 60  # Cache expiry time in seconds
data_key = "some_key"
cached_data = get_data_from_cache(data_key)
if cached_data:
    print("Data found in cache:", cached_data)
else:
    data = "Some data from the source"  # Replace this with your data-fetching logic
    add_data_to_cache(data_key, data)
    print("Fetched data:", data)
