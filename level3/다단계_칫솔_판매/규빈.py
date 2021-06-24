from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    dic = defaultdict(dict)

    for i in range(len(enroll)):
        dic[enroll[i]]['parent'] = referral[i]
        dic[enroll[i]]['pay'] = 0

    for i in range(len(seller)):
        total = amount[i] * 100
        point = total // 10
        current = seller[i]
        dic[current]['pay'] += total - point
        while point != 0 and dic[current]['parent'] != '-':
            total = point
            point //= 10
            current = dic[current]['parent']
            dic[current]['pay'] += total - point
    
    for name in enroll:
        answer.append(dic[name]['pay'])

    return answer