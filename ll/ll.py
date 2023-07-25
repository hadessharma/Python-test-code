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
        