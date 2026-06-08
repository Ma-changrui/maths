from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 100

def choice_Language():
    '''返回语言状态：True=英文, False=中文'''
    while True:
        choose = input('选择语言/Select Language(中文/English): ')
        if choose.lower() == 'english':
            return True
        elif choose == '中文':
            return False
        else:
            print('请选择语言/Please select a language.')

def L(cn, en, lang):
    '''根据 lang 返回中文或英文'''
    return en if lang else cn

def user_input(lang):
    '''获取用户输入，需要传入语言状态 lang'''
    numbers = []
    while True:
        try:
            prompt = L("输入数字(输入'q'退出)：",
                       "Enter a number (enter 'q' to quit): ",
                       lang)
            number = input(prompt)
        except EOFError:
            if not numbers:
                raise
            break
        if number == 'q':
            break
        try:
            num = Decimal(number)
        except (ValueError, InvalidOperation):
            print(L('必须为数字！', 'Must be a number.', lang))
        else:
            numbers.append(num)
    numbers.sort()
    return numbers

def average_value(data):
    '''计算所有分割点的左右两组及其平均值'''
    n = len(data)
    results = []
    for i in range(0, n - 1):
        left = data[:i+1]
        right = data[i+1:]
        left_mean = sum(left) / len(left)
        right_mean = sum(right) / len(right)
        results.append((i, left, right, left_mean, right_mean))
    return results