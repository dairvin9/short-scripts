class Node:
    next = None
    def __init__(self,data):
        self.value = data
    def __str__(self):
        return self.value
		
class LinkedList:
    def __init__(self,node):
        self.head = node          
    def __str__(self):
        node = self.head
        result = ""
        while node:
            result += node.value 
            result += " "
            node = node.next
        return result    
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

singly = LinkedList(a)
#print(singly)

def find_n_to_last_element(node,n):
    if node.next:
          result = find_n_to_last_element(node.next,n)
    if not node.next and n == 0:
        return node
    elif not node.next and n != 0:
        return n - 1    
    if isinstance(result,Node):
        return result
    elif result == 0:
        return node
    else: return result - 1
    
print(find_n_to_last_element(a,2))    