
def solution(enroll, referral, seller, amount):
    user = {}
    center = 0
    for i in range(len(enroll)):
        user[enroll[i]] = {
            'ref': referral[i], # 추천인
            'result': 0 # 총 수입
        }

    def add_result(name,pay): # 상향식 재귀 수입 계산
        if name == '-' or pay == 0:
            return pay
        up_pay = int(pay * 0.1)
        user[name]['result'] += (pay - up_pay)
        return add_result(user[name]['ref'], up_pay)

    for i in range(len(seller)):
        center += add_result(seller[i],amount[i]*100)

    return list(map(lambda x: x['result'],user.values()))

if __name__ == '__main__':
    print(solution(	["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))