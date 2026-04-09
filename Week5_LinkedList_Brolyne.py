# linkedlist
from turtle import position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


# usage Example


# create a new linked  list
my_list = LinkedList()

# check if the linked list is empty
print(my_list.is_empty())  # Output: True
my_list.head = Node(10)
my_list.head.next = Node(20)
my_list.head.next.next = Node(30)

# display the linked list

my_list.display()  # Output: 10 20 30 None# check if the linked list is empty
print(my_list.is_empty())  # Output: False


# insertion at the beginning
def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node


# Create list and insert elements
def create_list():
    my_list = LinkedList()
    my_list.head = Node(10)
    my_list.head.next = Node(20)
    my_list.head.next.next = Node(30)
    my_list.prepend(5)
    return my_list
my_list.display()  # Output: 5 10 20 30 None

# insertion at the end
def insert_at_end(self, data):
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
        return
    
    current = self.head
    # traverse to the end
    while current.next is not None:
        current = current.next

    # insert new node
    current.next = new_node

# usage example
def create_list():
    my_list = LinkedList()
    my_list.head = Node(10)
    my_list.head.next = Node(20)
    my_list.head.next.next = Node(30)
    my_list.prepend(5)
    my_list.insert_at_end(40)
    return my_list

my_list = create_list() # Output: 5 10 20 30 40 None
my_list.display()  # Output: 5 10 20 30 40 None

# insertion at a specific position
def insert_at_position(self, position, data):
    if position == 0:
        self.prepend(data)
        return
    
    new_node = Node(data)
    current = self.head

    # traverse to position
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of bounds")
        current = current.next

    # insert new node
    new_node.next = current.next
    current.next = new_node

# usage example
my_list.insert_at_position(2, 15)
my_list.display()  # Output: 5 10 15 20 30 40 None

#delete_by_value(value)- Delete first occurrence
def delete_by_value(self, value):
    if not self.head:
        print("List is empty")
        return False
    
    # If head contains the value
    if self.head.data == value:
        self.head = self.head.next
        return True
    
    # Search for the value in the list
    current = self.head
    while current.next and current.next.data != value:
        current = current.next

    if not current.next:
        print("Value not found in the list")
        return False
    
    # Delete by skipping the node
    current.next = current.next.next
    return True

# usage example
my_list.delete_by_value(15)
my_list.display()  # Output: 5 10 20 30 40 None

#search(value)- Find element, return index or -1
def search(self, value):
    current = self.head
    index = 0

    while current:
        if current.data == value:
            return index
        current = current.next
        index += 1

    return -1  # Value not found

# usage example
print(my_list.search(20))  # Output: 2
print(my_list.search(50))  # Output: -1

#display()- Print all elements in the list
def display(self):
    current = self.head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

#usage example
my_list.display()  # Output: 5 10 20 30 40 None

#is_empty()- Check if the list is empty
def is_empty(self):
    return self.head is None

#example usage
print(my_list.is_empty())  # Output: False
my_list.head = None
print(my_list.is_empty())  # Output: True

#size()- Return the number of elements in the list
def size(self):
    count = 0
    current = self.head

    while current:
        count += 1
        current = current.next

    return count

#example usage
print(my_list.size())  # Output: 0
my_list.head = Node(1)
my_list.head.next = Node(2)
print(my_list.size())  # Output: 2


       
    