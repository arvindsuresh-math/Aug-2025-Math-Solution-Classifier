def solve(
    quarters: int = 20,  # Alice has 20 quarters
    iron_nickel_value: int = 3,  # iron nickels worth $3 each
    iron_nickel_percentage: float = 0.2  # 20% of the nickels are iron nickels
):
    """Index: 95.
    Returns: the total value of Alice's money after exchanging quarters for nickels.
    """

    #: L1
    nickels_per_quarter = 4.0 # eval: 4.0 = 4.0

    #: L2
    total_nickels = quarters * nickels_per_quarter # eval: 80.0 = 20 * 4.0

    #: L3
    iron_nickels = total_nickels * iron_nickel_percentage # eval: 16.0 = 80.0 * 0.2

    #: L4
    regular_nickels = total_nickels - iron_nickels # eval: 64.0 = 80.0 - 16.0

    #: L5
    iron_nickels_total_value = iron_nickels * iron_nickel_value # eval: 48.0 = 16.0 * 3

    #: L6
    regular_nickels_total_value = regular_nickels * 0.05 # eval: 3.2 = 64.0 * 0.05

    #: FA
    answer = iron_nickels_total_value + regular_nickels_total_value
    return answer # eval: return 51.2
