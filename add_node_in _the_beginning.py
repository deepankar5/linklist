class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, number):
        temp = Node(number)
        temp.next = self.head
        self.head = temp


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