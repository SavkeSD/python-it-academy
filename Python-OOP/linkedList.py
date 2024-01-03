class Node:
    def __init__(self, data):
        self.data = data   # Assign data
        self.next = None   # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None

    # This function 
    def push(self, new_data):

        # Create a new node
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def pisi(self):
        pom = self.head
        while pom != None:
            print(pom.data,end=" ")
            pom = pom.next


if __name__ == '__main__':
    llist = LinkedList()

    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)

    llist.pisi()
