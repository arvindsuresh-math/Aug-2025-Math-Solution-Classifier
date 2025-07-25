def solve():
    """Index: 95.
    Returns: the total value of Alice's money after exchanging quarters for nickels, with some being iron nickels worth $3 each.
    """
    # L1
    quarter_value = 0.25 # A quarter is worth $0.25
    nickel_value = 0.05 # A nickel is worth $0.05
    nickels_per_quarter = quarter_value / nickel_value

    # L2
    num_quarters = 20 # Alice has 20 quarters
    total_nickels = num_quarters * nickels_per_quarter

    # L3
    iron_nickel_percent = 0.20 # 20% of the nickels are iron
    num_iron_nickels = total_nickels * iron_nickel_percent

    # L4
    num_regular_nickels = total_nickels - num_iron_nickels

    # L5
    iron_nickel_value = 3 # iron nickels worth $3 each
    total_iron_value = num_iron_nickels * iron_nickel_value

    # L6
    total_regular_value = num_regular_nickels * nickel_value

    # L7
    total_value = total_iron_value + total_regular_value

    # FA
    answer = total_value
    return answer