def solve():
    """Index: 5818.
    Returns: the number of nickels Tommy has.
    """
    # L1
    num_quarters = 4 # He has 4 quarters
    pennies_multiplier_quarters = 10 # 10 times as many pennies as quarters
    num_pennies = pennies_multiplier_quarters * num_quarters

    # L2
    dimes_more_than_pennies = 10 # 10 more dimes than pennies
    num_dimes = num_pennies + dimes_more_than_pennies

    # L3
    nickels_multiplier_dimes = 2 # twice as many nickels as dimes
    num_nickels = num_dimes * nickels_multiplier_dimes

    # FA
    answer = num_nickels
    return answer