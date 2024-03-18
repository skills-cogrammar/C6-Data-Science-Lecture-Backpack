from typing import Any, List

class ArrayNew:
    """
    A class representing an array with additional methods for manipulation.

    Methods:
    __init__(): Initialize an empty array.
    append(val: Any): Append a value to the end of the array.
    prepend(val: Any): Insert a value at the beginning of the array.
    delete_back() -> Any: Remove and return the last element of the array.
    delete_at(val: Any): Remove the first occurrence of a specified value from the array.
    delete_front(): Remove the first element of the array.
    print_list(): Print the current contents of the array.
    """
    def __init__(self) -> None:
        """
        Initialize an empty array.
        """
        self.data: List[Any] = []
        
    def append(self, val: Any) -> None:
        """
        Append a value to the end of the array.

        Parameters:
        val: The value to append.
        """
        self.data.append(val)
    
    def prepend(self, val: Any) -> None:
        """
        Insert a value at the beginning of the array.

        Parameters:
        val: The value to prepend.
        """
        self.data.insert(0, val)
    
    def delete_back(self) -> Any:
        """
        Remove and return the last element of the array.

        Returns:
        The last element of the array.
        """
        return self.data.pop()
    
    def delete_at(self, val: Any) -> None:
        """
        Remove the first occurrence of a specified value from the array.

        Parameters:
        val: The value to remove.
        """
        self.data.remove(val)
    
    def delete_front(self) -> None:
        """
        Remove the first element of the array.
        """
        self.data.remove(self.data[0])
    
    def print_list(self) -> None:
        """
        Print the current contents of the array.
        """
        print(self.data)


new_list = ArrayNew()
# new_list.append(1)
# new_list.prepend(2)
# new_list.append(3)
# new_list.prepend(4)
# new_list.print_list()
# new_list.delete_at(3)
# new_list.print_list()


import time

# Start timer
start_time = time.perf_counter()

# Analysis 
for i in range(0, 10000000):
    new_list.append(i)

# End timer
end_time = time.perf_counter()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)


