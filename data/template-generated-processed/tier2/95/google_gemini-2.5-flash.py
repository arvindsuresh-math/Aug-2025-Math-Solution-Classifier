def solve():
    """Index: 95.
    Returns: the total value of Alice's money.
    """
    # L1
    value_of_quarter = 0.25 # WK
    value_of_nickel = 0.05 # WK
    nickels_per_quarter = value_of_quarter / value_of_nickel

    # L2
    num_quarters = 20 # Alice has 20 quarters
    total_nickels = num_quarters * nickels_per_quarter

    # L3
    iron_nickel_percent_decimal = 0.20 # 20% of the nickels
    num_iron_nickels = total_nickels * iron_nickel_percent_decimal

    # L4
    num_regular_nickels = total_nickels - num_iron_nickels

    # L5
    value_iron_nickel = 3 # worth $3 each
    value_iron_nickels = num_iron_nickels * value_iron_nickel

    # L6
    value_regular_nickels = num_regular_nickels * value_of_nickel

    # L7
    total_value = value_iron_nickels + value_regular_nickels

    # FA
    answer = total_value
    return answer