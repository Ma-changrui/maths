from decimal import getcontext
from functools import partial
from ssbg import (
    average_value, choice_Language,
    L as _L,
    get_input as _get_input
)

getcontext().prec = 10

# 选择语言
lang = choice_Language()

# 用 partial 固定 lang 参数
L = partial(_L, lang=lang)
get_input = partial(_get_input, lang=lang)

# 获取至少 2 个数字
numbers = get_input(2)

# 计算分组
groups = average_value(numbers)
results = []

print("\n" + "─" * 48)

for i, left, right, left_mean, right_mean in groups:
    ssw = sum((x - left_mean) ** 2 for x in left) + \
          sum((x - right_mean) ** 2 for x in right)

    print(L(f"方案 {i + 1}", f"Plan {i + 1}"))
    
    print(L(f"  左组: {', '.join(str(x) for x in left)}",
             f"  Left: {', '.join(str(x) for x in left)}"))
    
    print(L(f"  右组: {', '.join(str(x) for x in right)}",
             f"  Right: {', '.join(str(x) for x in right)}"))
    
    print(f"  SSW = {ssw}")
    print("─" * 48)
    results.append((ssw, left, right))

if not results:
    print(L("\n没有可用的分组结果，程序退出。",
             "\nNo available grouping results, exiting."))
    exit(0)

best_ssw, best_left, best_right = min(results)

print(L(f"\n{'  ✨ 最优分组 ':=^48}", f"\n{'  ✨ Best Grouping ':=^48}"))

print(L(f"  左组: {', '.join(str(x) for x in best_left)}",
         f"  Left: {', '.join(str(x) for x in best_left)}"))

print(L(f"  右组: {', '.join(str(x) for x in best_right)}",
         f"  Right: {', '.join(str(x) for x in best_right)}"))

print(L(f"  最小组内离差平方和 = {best_ssw}",
         f"  Minimum SSW = {best_ssw}"))

if best_ssw.adjusted() <= 10:
    print(L(f"  四舍五入到 0.0001 = {format(best_ssw, '.4f')}",
             f"  Rounded to 0.0001 = {format(best_ssw, '.4f')}"))
else:
    print(L(f"  数值过大，使用科学计数法 = {format(best_ssw, '.4e')}",
             f"  Value too large, scientific notation = {format(best_ssw, '.4e')}"))
print("=" * 52)