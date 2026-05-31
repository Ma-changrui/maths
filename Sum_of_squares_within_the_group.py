from decimal import Decimal, getcontext, InvalidOperation

# 根据需要调整精度位数
getcontext().prec = 100

numbers = []

# 输入部分
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
n = len(numbers)

best_i = None
best_ssw = Decimal('Infinity')

for i in range(0, n - 1):          # i 从 0 到 n-2
    left = numbers[:i+1]           # 包含 i 位置的元素
    right = numbers[i+1:]          # 取 i 后面剩余的全部
    
    left_mean = sum(left) / len(left)
    right_mean = sum(right) / len(right)
    
    # 直接计算组内离差平方和
    ssw = sum((x - left_mean) ** 2 for x in left) + sum((x - right_mean) ** 2 for x in right)
    
    
    left_str = [str(x) for x in left]   # 每个 Decimal 转成字符串 '1', '2' 等
    right_str = [str(x) for x in right]
    print(f"i={i}: 左组 {left_str}, 右组 {right_str}, 组内离差平方和 = {ssw}")
    
    if ssw < best_ssw:
        best_ssw = ssw
        best_i = i

best_left = numbers[:best_i+1]
best_right = numbers[best_i+1:]
print(f"\n最佳分组：左组 {best_left}, 右组 {best_right}")
print(f"最小组内离差平方和 = {best_ssw}")
print(f'四舍五入到0.0001：{best_ssw:.4f}')
