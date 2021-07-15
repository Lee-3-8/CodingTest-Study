def solution(n, k, cmd):
    li = [i for i in range(n)]
    idx = k
    remove_set = []
    for cm in cmd:
        cm = cm.split(" ")
        if cm[0] == "U":
            idx -= int(cm[1])

        elif cm[0] == "D":
            idx += int(cm[1])

        elif cm[0] == "C":  # 삭제
            if idx == len(li) - 1:  # 마지막 행인경우
                remove_set.append((li.pop(), idx))
                idx -= 1
            else:
                remove_set.append((li[idx], idx))
                del li[idx]

        elif cm[0] == "Z":  # 복구
            t = remove_set.pop()
            if t[1] <= idx:
                li.insert(t[1], t[0])
                idx += 1
            else:
                li.insert(t[1], t[0])

    result = ["X" for _ in range(n)]
    for i in li:
        result[i] = "O"

    return "".join(result)


if __name__ == "__main__":
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
