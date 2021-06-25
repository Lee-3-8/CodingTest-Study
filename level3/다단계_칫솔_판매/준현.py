from collections import defaultdict


def solution(enroll, referral, seller, amount):
    dic = defaultdict(list)
    for i in range(len(enroll)):
        if referral[i] == "-":
            dic[enroll[i]].append("center")
            dic[enroll[i]].append(0)
        else:
            dic[enroll[i]].append(referral[i])
            dic[enroll[i]].append(0)
    dic['center'].extend(['last', 0])
    for i in range(len(seller)):
        price = amount[i]*100
        dic[seller[i]][1] += price - price//10
        price //= 10
        node = dic[seller[i]][0]
        while node != 'last' and price != 0:
            dic[node][1] += price - price//10
            price //= 10
            node = dic[node][0]
    answer = []
    for i in enroll:
        answer.append(dic[i][1])

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
