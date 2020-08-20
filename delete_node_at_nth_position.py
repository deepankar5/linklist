
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def get_node_address_realtive_to_position(self, position):  # get the position of the node
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        return temp

    def delete(self, position):
        prev_node = LinkList.get_node_address_realtive_to_position(self, position-1)
        next_node = LinkList.get_node_address_realtive_to_position(self, position+1)
        prev_node.next = next_node 

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':

    llist = LinkList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = forth

    llist.delete(4)
    llist.print()