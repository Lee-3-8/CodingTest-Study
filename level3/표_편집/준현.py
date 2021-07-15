class Node():
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


def solution(n, k, cmd):
    answer = ['O']*n
    stack = []
    first_node = Node(0)
    current_node = first_node
    for i in range(1, n):
        new_node = Node(i)
        new_node.prev = first_node
        first_node.next = new_node
        first_node = new_node

    for i in range(k):
        current_node = current_node.next

    for i in cmd:
        if len(i) == 3:
            print("3", int(i[-1]))
            if i[0] == 'D':
                for i in range(int(i[-1])):
                    current_node = current_node.next
            else:
                for i in range(int(i[-1])):
                    current_node = current_node.prev
        else:
            print("1", i)
            if i[0] == 'C':
                stack.append(current_node)
                answer[current_node.data] = 'X'
                prev_node = current_node.prev
                next_node = current_node.next

                if next_node != None:
                    next_node.prev = prev_node
                if prev_node != None:
                    prev_node.next = next_node

                if next_node != None:
                    current_node = next_node
                else:
                    current_node = prev_node
            else:
                temp = stack.pop()
                answer[temp.data] = 'O'
                prev_node = temp.prev
                next_node = temp.next
                if prev_node != None:
                    prev_node.next = temp
                if next_node != None:
                    next_node.prev = temp

    return ''.join(answer)


n = 8
k = 2
cmd = ["U 2", "C", "D 3", "C", "D 2", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))

# test case 1

n = 8
k = 0
cmd = ["D 2", "C", "C", "C", "C", "C", "Z", "Z"]

# test case 2
n = 8
k = 0
cmd = ["C", "C", "C", "C", "C", "Z", "Z", "Z"]
print(solution(n, k, cmd))
