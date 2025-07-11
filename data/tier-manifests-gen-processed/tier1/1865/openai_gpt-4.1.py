def solve():
    """Index: 1865.
    Returns: the total number of coins Linda has altogether after receiving more from her mother.
    """
    # L1
    initial_dimes = 2 # 2 dimes
    mother_dimes = 2 # 2 more dimes
    total_dimes = initial_dimes + mother_dimes

    # L2
    initial_quarters = 6 # 6 quarters
    mother_quarters = 10 # 10 quarters
    total_quarters = initial_quarters + mother_quarters

    # L3
    dimes_and_quarters = total_quarters + total_dimes

    # L4
    multiplier_nickels = 2 # twice as many nickels as she has
    initial_nickels = 5 # 5 nickels
    mother_nickels = multiplier_nickels * initial_nickels

    # L5
    total_nickels = mother_nickels + initial_nickels

    # L6
    answer = dimes_and_quarters + total_nickels
    return answer