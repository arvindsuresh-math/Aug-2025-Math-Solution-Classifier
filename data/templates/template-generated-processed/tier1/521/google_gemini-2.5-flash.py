def solve():
    """Index: 521.
    Returns: the number of strawberries left for his mom.
    """
    # L1
    num_dozen_picked = 2 # 2 dozen strawberries
    dozen = 12 # WK
    total_picked_strawberries = num_dozen_picked * dozen

    # L2
    eaten_strawberries = 6 # eats 6
    strawberries_for_mom = total_picked_strawberries - eaten_strawberries

    # FA
    answer = strawberries_for_mom
    return answer