import re

def solution(dartResult):
    num_list = list(map(int, re.compile(r'\d+').findall(dartResult)))
    dart_list = re.compile(r'[A-Z]\*?\#?').findall(dartResult)

    for i in range(3):
        
        if 'D' in dart_list[i]:
            num_list[i] **= 2
        elif 'T' in dart_list[i]:
            num_list[i] **= 3
        
        if '*' in dart_list[i]:
            num_list[i] *= 2
            if i > 0:
                num_list[i-1] *= 2
        elif '#' in dart_list[i]:
            num_list[i] *= -1
    
    return sum(num_list)


if __name__ == '__main__':
    result = solution('1T2D3D#')
    print(result)