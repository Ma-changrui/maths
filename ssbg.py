from decimal import Decimal, getcontext, InvalidOperation

getcontext().prec = 100


def user_input():
    '''获取用户输入，返回排序后的列表'''
    numbers = []
    while True:
        number = input("输入数字(输入'q'退出)：")
        if number == 'q':
            break
        else:
            try:
                num = Decimal(number)
            except (ValueError, InvalidOperation):
                print('必须为数字！')
            else:
                numbers.append(num)
    numbers.sort()
    return numbers


def average_value(data):
    '''计算所有分割点的左右两组平均值，返回列表 [(i, left_mean, right_mean), ...]'''
    n = len(data)
    results = []
    for i in range(0, n - 1):          # i 从 0 到 n-2
        left = data[:i+1]              # 包含 i 位置的元素
        right = data[i+1:]             # 取 i 后面剩余的全部
        
        left_mean = sum(left) / len(left)
        right_mean = sum(right) / len(right)
        
        results.append((i, left_mean, right_mean))
    
    return results


if __name__ == '__main__':
    numbers = user_input()
    print(numbers)
    means = average_value(numbers)
    print(means)
    for i, lm, rm in means:
        print(f"i={i}: 左组均值 = {lm}, 右组均值 = {rm}")