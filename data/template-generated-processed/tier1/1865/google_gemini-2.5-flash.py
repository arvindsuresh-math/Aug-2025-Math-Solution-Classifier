def solve():
    """Index: 1865.
    Returns: the total number of coins Linda has altogether.
    """
    # L1
    initial_dimes = 2 # 2 dimes
    mother_gave_dimes = 2 # 2 more dimes
    total_dimes = initial_dimes + mother_gave_dimes

    # L2
    initial_quarters = 6 # 6 quarters
    mother_gave_quarters = 10 # 10 quarters
    total_quarters = initial_quarters + mother_gave_quarters

    # L3
    total_dimes_quarters = total_quarters + total_dimes

    # L4
    initial_nickels = 5 # 5 nickels
    multiplier_twice = 2 # twice as many nickels
    mother_gave_nickels = multiplier_twice * initial_nickels

    # L5
    total_nickels = mother_gave_nickels + initial_nickels

    # L6
    total_coins = total_dimes_quarters + total_nickels

    # FA
    answer = total_coins
    return answer