def solve(
    quarters: int = 20,  # Alice has 20 quarters
    iron_nickel_value: int = 3,  # iron nickels worth $3 each
    iron_nickel_percentage: float = 0.2  # 20% of the nickels are iron nickels
):
    """Index: 95.
    Returns: the total value of Alice's money after exchanging quarters for nickels.
    """

    #: L1
    nickels_per_quarter = 0.25 / 0.05

    #: L2
    total_nickels = quarters * nickels_per_quarter

    #: L3
    iron_nickels = total_nickels * iron_nickel_percentage

    #: L4
    regular_nickels = total_nickels - iron_nickels

    #: L5
    iron_nickels_total_value = iron_nickels * iron_nickel_value

    #: L6
    regular_nickels_total_value = iron_nickel_value * 0.05

    #: FA
    answer = iron_nickels_total_value + regular_nickels_total_value
    return answer