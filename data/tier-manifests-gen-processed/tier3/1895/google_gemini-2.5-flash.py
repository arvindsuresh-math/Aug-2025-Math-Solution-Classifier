def solve():
    """Index: 1895.
    Returns: the total kilometers Natalia rode.
    """
    # L1
    tuesday_kilometers = 50 # on Tuesday 50 kilometers
    wednesday_reduction_divisor = 2 # 50% fewer kilometers than the day before
    wednesday_kilometers = tuesday_kilometers / wednesday_reduction_divisor

    # L2
    monday_kilometers = 40 # On Monday she rode 40 kilometers
    thursday_kilometers = monday_kilometers + wednesday_kilometers

    # L3
    total_kilometers = monday_kilometers + tuesday_kilometers + wednesday_kilometers + thursday_kilometers

    # FA
    answer = total_kilometers
    return answer