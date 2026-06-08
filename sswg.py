from decimal import getcontext
from ssbg import user_input, average_value, choice_Language, L


getcontext().prec = 10

# 选择语言，得到 lang
lang = choice_Language()

# 输入部分：重复直到获得至少两个数字
while True:
    try:
        numbers = user_input(lang)   # 传入 lang
    except EOFError:
        print(L("\n检测到输入中断（EOF），请重新输入。",
                 "\nInput interrupted (EOF), please re-enter.",
                 lang))
        continue
    if len(numbers) >= 2:
        break
    print(L("至少需要输入 2 个数字，请重新输入。\n",
            "At least 2 numbers are required, please re-enter.\n",
            lang))

# 计算分组
groups = average_value(numbers)
results = []

print("\n" + "─" * 48)

for i, left, right, left_mean, right_mean in groups:
    ssw = sum((x - left_mean) ** 2 for x in left) + \
          sum((x - right_mean) ** 2 for x in right)

    print(L(f"方案 {i + 1}", f"Plan {i + 1}", lang))
    print(L(f"  左组: {', '.join(str(x) for x in left)}",
             f"  Left: {', '.join(str(x) for x in left)}",
             lang))
    print(L(f"  右组: {', '.join(str(x) for x in right)}",
             f"  Right: {', '.join(str(x) for x in right)}",
             lang))
    print(f"  SSW = {ssw}")
    print("─" * 48)
    results.append((ssw, left, right))

if not results:
    print(L("\n没有可用的分组结果，程序退出。",
             "\nNo available grouping results, exiting.",
             lang))
    exit(0)

best_ssw, best_left, best_right = min(results)

print(L(f"\n{'  ✨ 最优分组 ':=^48}", f"\n{'  ✨ Best Grouping ':=^48}", lang))
print(L(f"  左组: {', '.join(str(x) for x in best_left)}",
         f"  Left: {', '.join(str(x) for x in best_left)}",
         lang))
print(L(f"  右组: {', '.join(str(x) for x in best_right)}",
         f"  Right: {', '.join(str(x) for x in best_right)}",
         lang))
print(L(f"  最小组内离差平方和 = {best_ssw}",
         f"  Minimum SSW = {best_ssw}",
         lang))

if best_ssw.adjusted() <= 10:
    print(L(f"  四舍五入到 0.0001 = {format(best_ssw, '.4f')}",
             f"  Rounded to 0.0001 = {format(best_ssw, '.4f')}",
             lang))
else:
    print(L(f"  数值过大，使用科学计数法 = {format(best_ssw, '.4e')}",
             f"  Value too large, scientific notation = {format(best_ssw, '.4e')}",
             lang))
print("=" * 52)