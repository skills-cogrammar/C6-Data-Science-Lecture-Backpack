# Define a Node class to represent each element in the list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next reference to None

# Define a LinkedList class to represent the entire list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None
        self.tail = None

    # Method to print all elements in the list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")  # Print the data of each node
            cur_node = cur_node.next
        print("None")  # Indicate the end of the list

    # Method to add a new element at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        # If the list is not empty, traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node  # Link the last node to the new node
        self.tail = new_node

    # Method to add a new element at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the new head of the list

    def delete_at(self, key):
        cur_node = self.head

        # Case 1: Deleting the head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Case 2: Deleting a non-head node
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # If the key is not found in the list
        if cur_node is None:
            return

        # Unlink the node from the list
        prev.next = cur_node.next
        cur_node = None

# Creating an instance of LinkedList
linked_list = LinkedList()
# linked_list.append(3)  # Appending 3 to the list
# linked_list.append(5)  # Appending 5 to the list
# linked_list.prepend(1) # Prepending 1 to the list
# linked_list.print_list()  # Output: 1 -> 3 -> 5 -> None

# linked_list.delete_at(5)  # Deleting 5 from the list
# linked_list.print_list()  # Output: 1 -> 3 -> None

import time

# Start timer
start_time = time.perf_counter()

# Analysis 
for i in range(0, 10000000):
    linked_list.append(i)

# End timer
end_time = time.perf_counter()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)

