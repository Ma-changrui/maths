from decimal import Decimal, getcontext
from ssbg import user_input, average_value

# 根据需要调整精度位数
getcontext().prec = 10

# 输入部分：直接调用 ssbg 中的 user_input 函数
numbers = user_input()

while len(numbers) < 2:
    print("至少需要输入 2 个数字才能分组。")
    numbers = user_input()

# 调用 ssbg 获取所有分割点的分组及均值
groups = average_value(numbers)

results = []

# 遍历已算好的 (i, left, right, left_mean, right_mean)，纯比较
print("\n" + "─" * 48)

for i, left, right, left_mean, right_mean in groups:
    # 直接计算组内离差平方和
    ssw = sum((x - left_mean) ** 2 for x in left) + \
        sum((x - right_mean) ** 2 for x in right)

    left_str = ', '.join(str(x) for x in left)
    right_str = ', '.join(str(x) for x in right)
    print(f"方案 {i + 1}")
    print(f"  左组: {left_str}")
    print(f"  右组: {right_str}")
    print(f"  SSW = {ssw}")
    print("─" * 48)

    results.append((ssw, left, right))

# min 按元组第一个元素 (ssw) 比较，解包拿到最优组合
best_ssw, best_left, best_right = min(results)

print(f"\n{'  ✨ 最优分组 ':=^48}")
print(f"  左组: {', '.join(str(x) for x in best_left)}")
print(f"  右组: {', '.join(str(x) for x in best_right)}")
print(f"  最小组内离差平方和 = {best_ssw}")
if best_ssw.adjusted() <= 10:   # 指数 <= 10 时才认为可以量化到 0.0001
    print(f"  四舍五入到 0.0001 = {format(best_ssw, '.4f')}")
else:
    print(f"  数值过大，使用科学计数法 = {format(best_ssw, '.4e')}")
print("=" * 52)
