def solve():
    """Index: 7191.
    Returns: the total money Sally can make from selling seashells.
    """
    # L1
    monday_seashells = 30 # 30 seashells on Monday
    half_divisor = 2 # half as many seashells
    tuesday_seashells = monday_seashells / half_divisor

    # L2
    total_seashells = monday_seashells + tuesday_seashells

    # L3
    price_per_seashell = 1.20 # $1.20
    total_money = total_seashells * price_per_seashell

    # FA
    answer = total_money
    return answer