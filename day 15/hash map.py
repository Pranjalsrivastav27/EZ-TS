class HashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        # Add a key-value pair to the hashmap
        self.map[key] = value

    def get(self, key):
        # Retrieve the value associated with a key
        if key in self.map:
            return self.map[key]
        else:
            return None

    def remove(self, key):
        # Remove a key-value pair from the hashmap
        if key in self.map:
            del self.map[key]

    def contains(self, key):
        # Check if the hashmap contains a key
        return key in self.map

    def size(self):
        # Get the number of key-value pairs in the hashmap
        return len(self.map)

    def keys(self):
        # Get a list of all keys in the hashmap
        return list(self.map.keys())

    def values(self):
        # Get a list of all values in the hashmap
        return list(self.map.values())

# Example usage:
my_hashmap = HashMap()
my_hashmap.put("apple", 5)
my_hashmap.put("banana", 3)

print("Value for 'apple':", my_hashmap.get("apple"))
print("Value for 'cherry':", my_hashmap.get("cherry"))

my_hashmap.remove("banana")
print("Value for 'banana' after removal:", my_hashmap.get("banana"))

print("Size of the hashmap:", my_hashmap.size())
print("Keys in the hashmap:", my_hashmap.keys())
print("Values in the hashmap:", my_hashmap.values())
class HashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        # Add a key-value pair to the hashmap
        self.map[key] = value

    def get(self, key):
        # Retrieve the value associated with a key
        if key in self.map:
            return self.map[key]
        else:
            return None

    def remove(self, key):
        # Remove a key-value pair from the hashmap
        if key in self.map:
            del self.map[key]

    def contains(self, key):
        # Check if the hashmap contains a key
        return key in self.map

    def size(self):
        # Get the number of key-value pairs in the hashmap
        return len(self.map)

    def keys(self):
        # Get a list of all keys in the hashmap
        return list(self.map.keys())

    def values(self):
        # Get a list of all values in the hashmap
        return list(self.map.values())

# Example usage:
my_hashmap = HashMap()
my_hashmap.put("apple", 5)
my_hashmap.put("banana", 3)

print("Value for 'apple':", my_hashmap.get("apple"))
print("Value for 'cherry':", my_hashmap.get("cherry"))

my_hashmap.remove("banana")
print("Value for 'banana' after removal:", my_hashmap.get("banana"))

print("Size of the hashmap:", my_hashmap.size())
print("Keys in the hashmap:", my_hashmap.keys())
print("Values in the hashmap:", my_hashmap.values())
