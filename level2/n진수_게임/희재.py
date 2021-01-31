def get_base_str(num, base):
    result = ""
    while num > 0:
        result = format(num % base, 'x') + result
        num //= base
    return result.upper() if result else "0"

def solution(n, t, m, p):
    num, buffer = 0, ""
    while len(buffer) < t * m:
        buffer += get_base_str(num, n)
        num += 1
    return "".join([buffer[i] for i in range(p-1, t*m, m)])