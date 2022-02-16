#参考代码，如嫌啰嗦，建议删除，一行搞定
def solve_it():
    '''
    pythontip oj不同于传统oj，代码里面直接使用变量，无需要提前声明，免去复杂的输入解析
    life is short, so i user python~
    you can use variables a
    '''
    b = []
    for index, char in enumerate(a):
        if char >= 'A' and char <= 'Z':
            temp = chr(ord(a[index]) - (ord('A') - ord('a')))
        else:
            temp = char
        b.append(temp)
    return ''.join(b) #your answer

print(solve_it())  # 答案需要输出
