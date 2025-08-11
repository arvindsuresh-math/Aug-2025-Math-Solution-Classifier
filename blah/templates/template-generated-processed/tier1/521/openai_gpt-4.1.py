def solve():
    """Index: 521.
    Returns: the number of strawberries Micah saves for his mom.
    """
    # L1
    num_dozen = 2 # 2 dozen strawberries
    dozen = 12 # WK
    total_strawberries = num_dozen * dozen

    # L2
    micah_eats = 6 # eats 6
    strawberries_for_mom = total_strawberries - micah_eats

    # FA
    answer = strawberries_for_mom
    return answer