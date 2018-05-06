from functools import reduce
def problem1(digits):
    if '' == digits: return 0
    kvmaps = {
            'A': '1',
            'D': '1',
            'G': '1',
            'J': '1',
            'M': '1',
            'P': '1',
            'T': '1',
            'W': '1',
            'B': '2',
            'E': '2',
            'H': '2',
            'K': '2',
            'N': '2',
            'Q': '2',
            'U': '2',
            'X': '2',
            'C': '3',
            'F': '3',
            'I': '3',
            'L': '3',
            'O': '3',
            'R': '3',
            'V': '3',
            'Y': '3',
            'S': '4',
            'Z': '4',
        }
    l = reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])#函数，digits是迭代对象，[]是初始值
    result = 0
    for i in l:
        result =int(i)
    newresult = 0
    while result != 0:
        newresult += result % 10
        result //= 10
    return(newresult)

         
print(problem1("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))