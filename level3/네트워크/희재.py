def solution(n, computers):
    disjoint = [i for i in range(n)]
    get_root = lambda x: x if disjoint[x] == x else get_root(disjoint[x])

    for idx, conns in enumerate(computers):
        for jdx, is_connected in enumerate(conns):
            if is_connected:
                disjoint[get_root(jdx)] = get_root(idx)

    for i in range(n):
        disjoint[i] = get_root(i)

    return len(set(disjoint))


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))