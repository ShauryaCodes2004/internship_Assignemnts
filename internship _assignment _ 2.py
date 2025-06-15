class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as null

    def append(self, data):
        """Add a node at the end of the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the end of the list and append
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements in the linked list"""
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise Exception("Index should be a positive integer.")

            # If deleting the first node
            if n == 1:
                print(f"Deleting node at position {n}: {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            prev = None

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if current is None:
                raise Exception(f"Index {n} is out of range.")

            print(f"Deleting node at position {n}: {current.data}")
            prev.next = current.next

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    ll = LinkedList()

    # Add elements to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

    print("Initial linked list:")
    ll.print_list()

    # Delete 3rd node (value 30)
    ll.delete_nth_node(3)
    print("After deleting 3rd node:")
    ll.print_list()

    # Attempt to delete out-of-range index
    ll.delete_nth_node(10)

    # Delete 1st node
    ll.delete_nth_node(1)
    print("After deleting 1st node:")
    ll.print_list()

    # Clear list and try deleting from empty
    ll = LinkedList()
    ll.delete_nth_node(1)
