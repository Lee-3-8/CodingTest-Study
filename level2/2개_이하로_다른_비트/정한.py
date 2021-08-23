def solution(numbers):
    result = []
    for i in numbers:
        temp = list(format(i, "b"))
        for idx in range(len(temp) - 1, -1, -1):

            if temp[idx] == "0":
                temp[idx] = "1"
                break

            if idx == 0:
                temp = ["1"] + temp

                break

        if idx != len(temp) - 1:
            for d_idx in range(idx + 1, len(temp)):
                if temp[d_idx] == "1":
                    temp[d_idx] = "0"
                    break
        result.append(int("".join(temp), 2))

    return result


if __name__ == "__main__":
    print(solution([2, 7]))
