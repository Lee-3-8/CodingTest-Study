from collections import defaultdict


def solution(enroll, referral, seller, amount):
    dic = dict()
    dic["center"] = [0, None]
    for i in range(0, len(enroll)):
        if referral[i] == "-":
            pa = "center"
        else:
            pa = referral[i]
        dic[enroll[i]] = [0, pa]

    for i in range(0, len(seller)):
        temp = seller[i]
        money = amount[i] * 100
        while dic[temp][1] != None:
            up_money = money // 10
            dic[temp][0] += money - up_money
            money = up_money
            temp = dic[temp][1]
            if up_money == 0:
                break

    result = []
    for i in enroll:
        result.append(dic[i][0])

    return result


if __name__ == "__main__":
    print(
        solution(
            ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["young", "john", "tod", "emily", "mary"],
            [12, 4, 2, 5, 10],
        )
    )
    # 	[360, 958, 108, 0, 450, 18, 180, 1080]
