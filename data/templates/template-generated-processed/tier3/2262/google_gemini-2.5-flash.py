def solve():
    """Index: 2262.
    Returns: the number of days Becky packs her lunch.
    """
    # L1
    total_school_days = 180 # 180 school days
    aliyah_frequency_divisor = 2 # half the time
    aliyah_lunch_days = total_school_days / aliyah_frequency_divisor

    # L2
    becky_frequency_divisor = 2 # half as much as Aliyah
    becky_lunch_days = aliyah_lunch_days / becky_frequency_divisor

    # FA
    answer = becky_lunch_days
    return answer