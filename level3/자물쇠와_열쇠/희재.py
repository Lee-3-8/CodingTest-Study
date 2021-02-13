def rotate(arr):
    return list(zip(*arr[::-1]))

def padding(key_len, lock_len, lock):
    pad = [[0] * (key_len * 2 + lock_len) for _ in range(key_len * 2 + lock_len)]
    for i in range(lock_len):
        for j in range(lock_len):
            pad[key_len + i][key_len + j] = lock[i][j]
    return pad

def pick(key, pad, right, bottom, attach):
    attach = 1 if attach else -1
    for i in range(len(key)):
        for j in range(len(key)):
            pad[bottom + i][right + j] += attach * key[i][j]

def is_allright(pad, key_len, lock_len):
    for i in range(lock_len):
        for j in range(lock_len):
            if pad[key_len + i][key_len + j] != 1:
                return False
    return True

def solution(key, lock):
    pad = padding(len(key), len(lock), lock)

    for _ in range(4):
        key = rotate(key)
        for bottom in range(1, len(key) + len(lock)):
            for right in range(1, len(key) + len(lock)):
                pick(key, pad, right, bottom, attach=True)
                if is_allright(pad, len(key), len(lock)):
                    return True
                pick(key, pad, right, bottom, attach=False)

    return False
