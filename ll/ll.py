class Node:
    def __init__(self, val) -> None:
        self.val  = val
        self.next = None
        
class LinkedList:
    def __init__(self, val) -> None:
        new_node  = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self) -> None:
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
    
    def append_list(self, val) -> None:
        temp = self.head
        new_node = Node(val=val)
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.tail = new_node
            
        