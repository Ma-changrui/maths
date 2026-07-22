from decimal import Decimal
from ssbg import choice_Language, L as _L, get_input as _get_input
from functools import partial

# 选择语言
lang = choice_Language()
L = partial(_L, lang=lang)
get_input = partial(_get_input, lang=lang)

# 获取至少 4 个数字
numbers = get_input(4)


def median(data):
    """求中位数"""
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / Decimal('2')


def quartiles(data):
    """
    返回 (Q1, Q2, Q3)
    数据个数 >= 4
    """
    n = len(data)
    if n < 4:
        return None, None, None

    # 中位数 Q2
    q2 = median(data)

    # 分成上下两半（不包含中位数本身）
    if n % 2 == 1:          # 奇数个：跳过正中间那个
        lower = data[:n // 2]
        upper = data[n // 2 + 1:]
    else:                   # 偶数个：直接分成等长的两半
        lower = data[:n // 2]
        upper = data[n // 2:]

    q1 = median(lower)
    q3 = median(upper)
    return q1, q2, q3


# ========== 计算并显示 ==========

q1, q2, q3 = quartiles(numbers)

print("\n" + "=" * 52)
print(L(f"原始数据（已排序）: {', '.join(str(x) for x in numbers)}",
         f"Data (sorted): {', '.join(str(x) for x in numbers)}"))
print(L(f"数据个数 n = {len(numbers)}",
         f"Count n = {len(numbers)}"))
print("=" * 52)

print(L("\n📊 四分位数与五数概括",
         "\n📊 Quartiles & Five-Number Summary"))
print(L(f"  最小值 Min : {numbers[0]}",
         f"  Minimum   : {numbers[0]}"))
print(L(f"  第一四分位数 Q1 : {q1}",
         f"  First Quartile  : {q1}"))
print(L(f"  中位数 Q2 (Med) : {q2}",
         f"  Median          : {q2}"))
print(L(f"  第三四分位数 Q3 : {q3}",
         f"  Third Quartile  : {q3}"))
print(L(f"  最大值 Max : {numbers[-1]}",
         f"  Maximum   : {numbers[-1]}"))

# 四分位距与异常值检测
iqr = q3 - q1
lower_fence = q1 - Decimal('1.5') * iqr
upper_fence = q3 + Decimal('1.5') * iqr
outliers = [x for x in numbers if x < lower_fence or x > upper_fence]

print(L(f"\n📊 异常值检测（箱线图 IQR × 1.5 法则）",
         f"\n📊 Outlier Detection (IQR × 1.5 Rule)"))
print(L(f"  下界 Lower Fence: {lower_fence}",
         f"  Lower Fence: {lower_fence}"))
print(L(f"  上界 Upper Fence: {upper_fence}",
         f"  Upper Fence: {upper_fence}"))
if outliers:
    print(L(f"  ⚠️ 异常值: {', '.join(str(x) for x in outliers)}",
             f"  ⚠️ Outliers: {', '.join(str(x) for x in outliers)}"))
else:
    print(L(f"  ✅ 无异常值",
             f"  ✅ No outliers"))
print("=" * 52)