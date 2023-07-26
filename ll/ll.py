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
    
    def prepend(self, val: int) -> bool:
        new_node = Node(val=val)
        if not self.head:
            self.head, self.tail = new_node, new_node
            self.length+=1
            return True
        
        new_node.next  = self.head
        self.head      = new_node
        self.length   += 1
        return True
        
    def pop_first(self):
        if not self.head:
            return None
        
        popped       = self.head
        
        if not self.head.next:
            self.head    = None
            self.tail    = None
            self.length -= 1
            return popped
        
        self.head    = self.head.next
        self.length -= 1
        
        return popped
    
    def get(self, index):
        if not self.head or self.length <= index:
            return None
        
        temp  = self.head
        count = 0
        
        while temp:
            if count == index:
                return temp
            count+=1
            temp = temp.next
        
        return None
    
    def set_value(self, index, val):
        temp = self.get(index=index)
        if temp:
            temp.val = val
            return True
        return False
    
    def reverse(self):
        if not self.head or not self.head.next:
            return None
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        pre = None
        
        while temp:
            n = temp.next
            temp.next = pre
            pre = temp
            temp = n
            