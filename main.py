from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_structure(structure):
    print("Current state:", structure)


def stack_menu(stack):
    while True:
        print("\nSTACK OPERATIONS")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("0. Back")
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                print("Value pushed.")
            elif choice == "2":
                print("Popped:", stack.pop())
            elif choice == "3":
                print("Top element:", stack.peek())
            elif choice == "4":
                print("Is empty:", stack.is_empty())
            elif choice == "5":
                print("Is full:", stack.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
                continue
            show_structure(stack)
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_structure(stack)


def queue_menu(queue):
    while True:
        print("\nQUEUE OPERATIONS")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("0. Back")
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print("Value enqueued.")
            elif choice == "2":
                print("Dequeued:", queue.dequeue())
            elif choice == "3":
                print("Front element:", queue.peek_front())
            elif choice == "4":
                print("Is empty:", queue.is_empty())
            elif choice == "5":
                print("Is full:", queue.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
                continue
            show_structure(queue)
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_structure(queue)


def choose_structure():
    print("\nSELECT DATA STRUCTURE")
    print("1. Array Stack")
    print("2. Linked List Stack")
    print("3. Circular Array Queue")
    print("4. Linked List Queue")
    print("5. Application Exercises")
    print("0. Exit")
    return input("Choose an implementation: ").strip()


def balanced_parentheses(expression):
    """Return True when (), [], and {} are correctly balanced."""
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    opening = set(matching.values())

    for character in expression:
        if character in opening:
            stack.append(character)
        elif character in matching:
            if not stack or stack.pop() != matching[character]:
                return False
    return not stack


def print_queue_simulation():
    """Demonstrate FIFO printing with job IDs and page counts."""
    jobs = []
    while True:
        print("\nPRINT QUEUE")
        print("1. Add print job")
        print("2. Print next job")
        print("3. Show waiting jobs")
        print("0. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            job_id = input("Enter job ID: ").strip()
            try:
                pages = int(input("Enter number of pages: "))
                if pages <= 0:
                    print("Page count must be greater than zero.")
                    continue
            except ValueError:
                print("Please enter a valid whole number.")
                continue
            jobs.append({"id": job_id, "pages": pages})
            print(f"Job {job_id} added. Waiting order:", [job["id"] for job in jobs])
        elif choice == "2":
            if not jobs:
                print("Print queue is empty.")
            else:
                job = jobs.pop(0)
                print(f"Printing job {job['id']} ({job['pages']} pages).")
                print("Remaining jobs:", [item["id"] for item in jobs])
        elif choice == "3":
            if jobs:
                print("Waiting order:", [f"{job['id']} ({job['pages']} pages)" for job in jobs])
            else:
                print("No waiting jobs.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def application_menu():
    while True:
        print("\nAPPLICATION EXERCISES")
        print("1. Balanced parentheses checker")
        print("2. Print queue simulation")
        print("0. Back")
        choice = input("Choose an exercise: ").strip()

        if choice == "1":
            expression = input("Enter an expression: ")
            if balanced_parentheses(expression):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are NOT balanced.")
        elif choice == "2":
            print_queue_simulation()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        choice = choose_structure()

        if choice == "1":
            try:
                capacity = int(input("Enter stack capacity: "))
                stack_menu(ArrayStack(capacity))
            except ValueError as error:
                print("Invalid capacity:", error)
        elif choice == "2":
            stack_menu(LinkedStack())
        elif choice == "3":
            try:
                capacity = int(input("Enter queue capacity: "))
                queue_menu(ArrayQueue(capacity))
            except ValueError as error:
                print("Invalid capacity:", error)
        elif choice == "4":
            queue_menu(LinkedQueue())
        elif choice == "5":
            application_menu()
        elif choice == "0":
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
