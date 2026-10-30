from linked_stack import Node


class LinkedQueue:
    """A queue implemented using a singly linked list with front and rear."""

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: no front element to view.")
        return self.front.value

    def __str__(self):
        values = []
        current = self.front
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return f"Front -> {' -> '.join(values)} -> Rear" if values else "Front -> None (empty)"
