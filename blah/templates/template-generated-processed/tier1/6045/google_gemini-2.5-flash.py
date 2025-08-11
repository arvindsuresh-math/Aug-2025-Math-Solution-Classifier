def solve():
    """Index: 6045.
    Returns: the total amount of money Billy and Sam have together.
    """
    # L1
    multiplier_for_twice = 2 # twice the money
    sam_money = 75 # Sam has $75
    less_than_twice = 25 # $25 less than twice
    twice_sam_money = multiplier_for_twice * sam_money
    billy_money = twice_sam_money - less_than_twice

    # L2
    total_money = sam_money + billy_money

    # FA
    answer = total_money
    return answer