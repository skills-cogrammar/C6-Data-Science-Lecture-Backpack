from typing import Any, List, Optional

class Queue:
    """
    A class representing a queue data structure.

    Attributes:
    - queue (List[Any]): A list to store the elements of the queue.
    - queue_size (Optional[int]): The maximum size of the queue, if specified.
    - pointer_position (int): The position of the pointer indicating the next position to insert an element.

    Methods:
    - __init__(queue_size: Optional[int] = None) -> None: Initializes an empty queue.
    - enqueue(value: Any) -> None: Adds an element to the rear of the queue.
    - dequeue() -> Any: Removes and returns the element from the front of the queue.
    - peek() -> None: Displays the element at the front of the queue without removing it.
    """

    def __init__(self, queue_size: Optional[int] = None) -> None:
        """
        Initializes an empty queue.

        Args:
        - queue_size (Optional[int]): The maximum size of the queue, if specified.
        """
        self.queue: List[Any] = []
        self.queue_size: Optional[int] = queue_size
        self.pointer_position: int = 0

    def enqueue(self, value: Any) -> None:
        """
        Adds an element to the rear of the queue.

        Args:
        - value (Any): The value to be added to the queue.
        """
        if self.queue_size is not None and self.pointer_position < self.queue_size:
            self.queue.insert(self.pointer_position, value)
            self.pointer_position += 1
        elif self.queue_size is None:
            self.queue.append(value)
        else:
            print("List FULL!")

    def dequeue(self) -> Any:
        """
        Removes and returns the element from the front of the queue.

        Returns:
        - Any: The element removed from the front of the queue, or None if the queue is empty.
        """
        if len(self.queue) == 0:
            print("Error: Queue Underflow!")
            return None
        else:
            return self.queue.pop(0)

    def peek(self) -> None:
        """
        Displays the element at the front of the queue without removing it.
        """
        if self.queue:
            print(self.queue[0])
        else:
            print("Error: Queue is empty!")

# Create a queue to test the class
queue = Queue(0)

# Check underflow error
queue.dequeue()

# Add some elements to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.peek()

# Remove an element from the queue
popped = queue.dequeue()
print(f"Dequeued element: {popped}")
