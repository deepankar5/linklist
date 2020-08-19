
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, position, value):
        new_node = Node(value)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(position-2):
            if temp is None:
                print('the given position don\'t exit')
                return
            else:
                temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print("The output value: ", temp.data)
            temp = temp.next

if __name__ == '__main__':
    position = int(input("Position at which the number have to inserted: "))
    value = int(input('Enter the number which has to be added: '))
    llist = LinkList()
    llist.insert(position, value)
    llist.print()


