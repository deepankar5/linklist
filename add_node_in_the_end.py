# Node class
class Node:
    # function to initiate the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Assign next as null

class Linklist:
    def __init__(self):
        self.head = None

    def insert(self, number):
        new_node = Node(number)
        # if the LinkList in empty then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        # else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        # change the next in the last node
        last.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print("output", temp.data)
            temp = temp.next


if __name__ == '__main__':
    numbers = int(input('Enter how much numbers you want to insert: '))
    llist = Linklist()
    for i in range(numbers):
        number = input('Enter the number: ')
        llist.insert(number)
    llist.print()
