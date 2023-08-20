class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
    
class LinkedList :
    def __init__(self) :
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
        else :
            new_node.next = self.head
            self.head = new_node
            # Print the linked list
    def print_list(self) :
        temp = self.head
        while temp :
            print(temp.data)
            temp = temp.next
    def delete_node(self,node):
        temp = self.head
        while temp :
            if temp.next == node:
                temp.next = node.next
                break
            temp = temp.next
lkdList = LinkedList()
lkdList.insert(10)
lkdList.insert(20)
lkdList.insert(30)
lkdList.print_list()
lkdList.delete_node(20)
lkdList.print_list()
        
    