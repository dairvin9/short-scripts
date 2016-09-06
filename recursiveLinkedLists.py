class Node:
    next = None
    def __init__(self,data):
        self.value = data
    def __str__(self):
        try:
            return str(self.value)
        except ValueError:
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
        
a = Node(3)
b = Node(1)
c = Node(5)


a.next = b
b.next = c

x = Node(5)
y = Node(9)
z = Node(2)


x.next = y
y.next = z


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
    
#print(find_n_to_last_element(a,2))   
def add_two_linked_lists(node1,node2):
    if node1.next:
        carry, next_node = add_two_linked_lists(node1.next,node2.next)
    else:
        carry = 0
        next_node = None
    new_node = Node((carry+node1.value+node2.value)%10)
    new_node.next = next_node
    new_carry = (carry+node1.value+node2.value)//10
    return new_carry,new_node
    
print(add_two_linked_lists(a,x)[1])   