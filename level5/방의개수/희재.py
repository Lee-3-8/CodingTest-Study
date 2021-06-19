MOVE = lambda cur, point: (cur[0] + point[0], cur[1] + point[1])
point = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

def solution(arrows):
    cur = (0, 0)
    V, E = set([cur]), set()
    for arrow in arrows:
        for _ in range(2):
            next_cur = MOVE(cur, point[arrow])
            V.add(next_cur)
            E.update([(cur, next_cur), (next_cur, cur)])
            cur = next_cur

    return len(E) // 2 - len(V) + 1

if __name__ == '__main__':
    print(solution([2, 5, 2, 7]))








"""
def solution(arrows):
    answer, cur = 0, (0, 0)
    v_node, v_direction = set([cur]), set()

    for arrow in arrows:
        for _ in range(2):
            next_cur = MOVE(cur, point[arrow])
            if (
                next_cur in v_node
                and (cur, next_cur) not in v_direction
            ):
                answer += 1
            v_node.add(next_cur)
            v_direction.update([(cur, next_cur), (next_cur, cur)])
            cur = next_cur

    return answer
"""
