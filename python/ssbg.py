from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 100

# ---------- 全局语言状态（模块私有） ----------

def choice_Language():

    while True:
        choose = input('选择语言/Select Language(中文/English): ')
        if choose.lower().strip() == 'english':
            return True
        elif choose.strip() == '中文':
            return False
        else:
            print('请选择语言/Please select a language.')

def L(cn, en, lang):
    return en if lang else cn

def user_input(lang):
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

def get_input(min_count, lang):
    '''要求用户至少输入 min_count 个数字，返回满足条件的数字列表'''
    while True:
        try:
            numbers = user_input(lang)
        except EOFError:
            print(L("\n检测到输入中断（EOF），请重新输入。",
                    "\nInput interrupted (EOF), please re-enter.",
                    lang))
            continue
        if len(numbers) >= min_count:
            return numbers
        print(L(f"至少需要输入 {min_count} 个数字，请重新输入。\n",
                f"At least {min_count} numbers are required, please re-enter.\n",
                lang))

def average_value(data):
    n = len(data)
    results = []
    for i in range(0, n - 1):
        left = data[:i+1]
        right = data[i+1:]
        left_mean = sum(left) / len(left)
        right_mean = sum(right) / len(right)
        results.append((i, left, right, left_mean, right_mean))
    return results