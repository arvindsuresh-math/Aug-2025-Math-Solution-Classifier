def solve():
    """Index: 4792.
    Returns: the number of clay pots Nancy created on Wednesday.
    """
    # L1
    monday_pots = 12 # 12 clay pots on Monday
    multiplier_tuesday = 2 # twice as many on Tuesday
    tuesday_pots = monday_pots * multiplier_tuesday

    # L2
    monday_tuesday_total = monday_pots + tuesday_pots

    # L3
    total_end_week = 50 # ends the week with 50 clay pots
    wednesday_pots = total_end_week - monday_tuesday_total

    # FA
    answer = wednesday_pots
    return answer