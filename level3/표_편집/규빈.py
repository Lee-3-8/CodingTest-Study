class DLL:
    class Node:
        def __init__(self, elem, fore, back):
            self.elem = elem
            self.prev = fore
            self.next = back
    
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.next = self.tail
        self.size = 0
    
    def insert(self, node, elem):
        prev = node.prev
        newNode = self.Node(elem, prev, node)
        node.prev = newNode
        prev.next = newNode
    
    def delete(self, node):
        fore = node.prev
        back = node.next
        fore.next = back
        back.prev = fore
        return node

def solution(n, k, cmd):
    answer = ['O'] * n
    reverse = []
    d = DLL()
    cur = d.head
    for i in range(n):
        d.insert(d.tail, i)
    
    for i in range(k+1):
        cur = cur.next
    
    for commend in cmd:
        op = commend.split()

        if op[0] == 'U':
            move = int(op[1])
            while cur.prev != d.head and move:
                cur = cur.prev
                move -= 1

        elif op[0] == 'D':
            move = int(op[1])
            while cur.next != d.tail and move:
                cur = cur.next
                move -= 1

        elif op[0] == 'C':

            if cur.next == d.tail:
                cur = cur.prev
                node = d.delete(cur.next)

            else:
                cur = cur.next
                node = d.delete(cur.prev)
                
            reverse.append(node)

        else: # Z
            node = reverse.pop()
            node.next.prev = node
            node.prev.next = node
    
    for node in reverse:
        answer[node.elem] = 'X'
    
    return "".join(answer)