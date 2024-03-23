from typing import Any, List, Optional
class Stack:
    """
    A class representing a stack data structure.

    Attributes:
    - max_size (int): The maximum capacity of the stack.
    - stack (List[Optional[Any]]): A list representing the stack.
    - top (int): Index of the top element in the stack.

    Methods:
    - __init__(max_size: int): Initializes an empty stack with the given maximum size.
    - push(value: Any) -> None: Pushes an element onto the stack.
    - pop() -> Any: Pops and returns the top element from the stack.
    """

    def __init__(self, max_size: int):
        """
        Initializes an empty stack with the given maximum size.

        Args:
        - max_size (int): The maximum capacity of the stack.
        """
        self.max_size: int = max_size
        self.stack: List[Optional[Any]] = [None] * max_size
        self.top: int = -1

    def push(self, value: Any) -> None:
        """
        Pushes an element onto the stack.

        Args:
        - value (Any): The value to be pushed onto the stack.
        """
        if self.top == self.max_size - 1:
            print("Error: Stack Overflow!")
            return

        self.top += 1
        self.stack[self.top] = value

    def peek(self) -> None:
        """
        Displays the element at the front of the queue without removing it.
        """
        if self.stack:
            print(self.stack[self.top])
        else:
            print("Error: Queue is empty!")

    def pop(self) -> Any:
        """
        Pops and returns the top element from the stack.

        Returns:
        - Any: The element popped from the top of the stack.
        """
        if self.top == -1:
            print("Error: Stack Underflow!")
            return

        removed = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return removed
    
    def print_stack(self) -> None:
        """
        Prints the elements of the stack.
        """
        print(self.stack)


# Example usage:
stack = Stack(10)

stack.pop()  # This will print "Error: Stack Underflow!" since the stack is empty

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.peek()
stack.pop()  # This will return 13, as it's the last element pushed onto the stack
stack.print_stack() # This will print the stack 


