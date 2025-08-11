from fractions import Fraction

def solve():
    """Index: 6596.
    Returns: the number of jelly beans Emmanuel will get.
    """
    # L1
    total_jelly_beans = 200 # jar of 200 jelly beans
    thomas_percentage_numerator = 10 # 10%
    thomas_percentage_denominator = 100 # 10%
    thomas_jelly_beans = total_jelly_beans * Fraction(thomas_percentage_numerator, thomas_percentage_denominator)

    # L2
    remaining_jelly_beans = total_jelly_beans - thomas_jelly_beans

    # L3
    barry_ratio_part = 4 # ratio 4:5
    emmanuel_ratio_part = 5 # ratio 4:5
    jelly_beans_per_share = remaining_jelly_beans / (barry_ratio_part + emmanuel_ratio_part)

    # L4
    emmanuel_jelly_beans = emmanuel_ratio_part * jelly_beans_per_share

    # FA
    answer = emmanuel_jelly_beans
    return answer