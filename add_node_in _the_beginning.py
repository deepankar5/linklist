class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, number):
        new_node = Node(number)
        # make the new_node next to head
        new_node.next = self.head
        # make the new_node head
        self.head = new_node


    def print(self):
        temp = self.head
        while(temp):
            print("linklist data: ", temp.data)
            temp = temp.next


if __name__ == '__main__':
    numbers = int(input("How many  number you want to insert: "))
    llist = LinkList()
    for i in range(numbers):
        number = input('Enter the number: ')
        llist.insert(number)
    llist.print()