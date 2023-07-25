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
    
    def append_list(self, val) -> bool:
        new_node = Node(val=val)
        
        if  not self.head:
            self.head    = new_node
            self.tail    = new_node
            self.length += 1
            return True
            
        temp = self.head
        
        while temp.next:
            temp = temp.next
            
        temp.next    = new_node
        self.tail    = new_node
        self.length += 1
        
        return True
        
    def pop(self):
        if not self.head:
            return None
        
        temp = self.head
        
        if not self.head.next:
            self.length -= 1
            self.head, self.tail = None, None
            return temp

        while temp.next.next:
            temp = temp.next
            
        self.tail       = temp
        popped          = temp.next
        self.tail.next  = None
        self.length    -= 1
        return popped