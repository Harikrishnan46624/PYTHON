# class HashTable:
#     def __init__(self,size) -> None:
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def hash(self, key):
#         return hash(key) % self.size
    
#     def insert(self,key,value):
#         hash_value = self.hash(key)
#         bucket = self.table[hash_value]
#         for i, (existing_key, _) in enumerate(bucket):
#             if existing_key == key:
#                 bucket[i] = (key, value)
#                 return
#         bucket.append((key, value))

#     def search(self, key):
#         hash_value = self.hash(key)
#         bucket = self.table[hash_value]
#         for existing_key, value in bucket:
#             if existing_key == key:
#                 return value
#         return None
    
#     def delete(self, key):
#         hash_value = self.hash(key)
#         bucket = self.table[hash_value]
#         for i, (existing_key, _) in enumerate(bucket):
#             if existing_key == key:
#                 del bucket[i]
#                 return
            

# hash_table = HashTable(10)
# hash_table.insert('apple', 5)
# hash_table.insert('banana', 2)
# hash_table.insert('orange', 8)

# print(hash_table.search('apple'))  # Output: 5
# print(hash_table.search('banana'))  # Output: 2
# print(hash_table.search('orange'))  # Output: 8
# print(hash_table.search('grape'))  # Output: None

# hash_table.delete('banana')
# print(hash_table.search('banana'))  # Output: None



# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def _hash_function(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         hash_value = self._hash_function(key)
#         bucket = self.table[hash_value]
#         print(hash_value,"some")

#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)  # Update existing key-value pair
#                 return
#         bucket.append((key, value))  # Add new key-value pair

#     def get(self, key):
#         hash_value = self._hash_function(key)
#         bucket = self.table[hash_value]
#         for k, v in bucket:
#             if k == key:
#                 return v
#         raise KeyError(f"Key '{key}' not found in the hash table.")

#     def remove(self, key):
#         hash_value = self._hash_function(key)
#         bucket = self.table[hash_value]

#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 return
#         raise KeyError(f"Key '{key}' not found in the hash table.")



# # Create a hash table with size 10
# hash_table = HashTable(10)

# # Insert key-value pairs
# hash_table.insert("apple", 5)
# hash_table.insert("banana", 10)
# hash_table.insert("orange", 3)

# # Retrieve values
# print(hash_table.get("apple"))  # Output: 5
# print(hash_table.get("banana"))  # Output: 10


# # Update value
# hash_table.insert("apple", 7)
# print(hash_table.get("apple"))  # Output: 7

# # Remove key
# hash_table.remove("banana")

# # Try to retrieve the removed key
# print(hash_table.get("banana"))  # Raises KeyError: Key 'banana' not found in the hash table.





class HashTable(object):
    def __init__(self, length=4):
        # Initiate our array with empty values.
        self.array = [None] * length
    
    def hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length
        
    def add(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
                else:
                # If no breaks was hit in the for loop, it 
                # means that no existing key was found, 
                # so we can simply just add it to the end.
                    self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate 
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])
    
    def get(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()
h = HashTable()
h.add("bannana",1)
h.add("apple",2)
print(h.get("apple"))


class HashTable(object):
    def __init__(self, length=4) -> None:
        self.array = [None] * length
        
    def hash(self,key):
        length = len(self.array)
        return hash(key) % length
    
    def add(self,key,value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] == value
                    break
                else:
                    self.array[index].append([key,value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self,key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
                raise KeyError()