import re
from collections import OrderedDict
def solution(s):
    orderd = sorted(s[1:-2].split('},'),key=lambda x: x.count(',')) # 앞뒤 "{제거 , 쪼개기 , ','수로 구분
    print(orderd)
    p = re.compile(r'\d+').findall("".join(orderd))
    print(p)
    result = list(OrderedDict.fromkeys(p))
    result = list(map(lambda x: int(x),result))
    print(result)
    return result

solution("{{20,111},{111}}")
