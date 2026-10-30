# Stacks and Queues: Array vs. Linked List

## Description
This Python program demonstrates four fundamental data structures:
- Array Stack
- Linked List Stack
- Circular Array Queue
- Linked List Queue

It also includes a balanced-parentheses checker and a print-queue simulation.

## Requirements
- Python 3.8 or later
- No external libraries are required

## Files
| File | Description |
|---|---|
| `array_stack.py` | Fixed-capacity stack using a Python list |
| `linked_stack.py` | Stack using a singly linked list |
| `array_queue.py` | Circular queue using a Python list |
| `linked_queue.py` | Queue using linked nodes with front and rear references |
| `main.py` | Menu-driven test driver and application exercises |
| `analysis.md` | Written answer to the analysis question |

## How to Run
1. Place all six Python/Markdown files in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python main.py
   ```

4. Select an implementation from the main menu and perform its operations.
5. For the application exercises, select option `5` from the main menu.

## Features
- Stack operations: `push`, `pop`, `peek`, `is_empty`, and `is_full`
- Queue operations: `enqueue`, `dequeue`, `peek_front`, `is_empty`, and `is_full`
- Descriptive underflow and overflow exceptions
- Circular array queue with wrap-around
- State display after each successful operation and after errors
- Balanced-parentheses checking for `()`, `[]`, and `{}`
- FIFO print-queue simulation

## Notes
Array-based structures have a fixed capacity. Linked-list structures do not have a fixed capacity and are limited by available memory. The program raises clear errors when an operation is attempted on an empty structure or when an array-based structure is full.
