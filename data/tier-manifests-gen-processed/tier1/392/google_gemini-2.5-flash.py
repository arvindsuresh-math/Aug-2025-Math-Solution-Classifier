def solve():
    """Index: 392.
    Returns: the total minutes to wash everything.
    """
    # L1
    clothes_wash_time = 30 # The clothes take 30 minutes to wash
    multiplier_twice = 2 # twice as long
    towels_wash_time = clothes_wash_time * multiplier_twice

    # L2
    minutes_less_sheets = 15 # 15 minutes less time
    sheets_wash_time = towels_wash_time - minutes_less_sheets

    # L3
    total_wash_time = clothes_wash_time + towels_wash_time + sheets_wash_time

    # FA
    answer = total_wash_time
    return answer