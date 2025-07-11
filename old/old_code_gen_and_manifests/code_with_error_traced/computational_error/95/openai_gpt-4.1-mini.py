def solve(
    num_quarters: int = 20,  # Alice has 20 quarters
    iron_nickel_value: int = 3,  # iron nickels worth $3 each
    iron_nickel_fraction: float = 0.20,  # 20% of the nickels are iron nickels
    regular_nickel_value: float = 0.05  # regular nickels worth $0.05 each
):
    """Index: 95.
    Returns: the total value of Alice's money after exchanging quarters for nickels including iron nickels.
    """

    #: L1
    nickels_per_quarter = 0.25 / 0.05 # eval: 5.0 = 0.25 / 0.05

    #: L2
    total_nickels = num_quarters * nickels_per_quarter # eval: 100.0 = 20 * 5.0

    #: L3
    iron_nickels = total_nickels * iron_nickel_fraction # eval: 20.0 = 100.0 * 0.2

    #: L4
    regular_nickels = 70.0 # eval: 70.0 = 70.0

    #: L5
    iron_nickels_value = iron_nickels * iron_nickel_value # eval: 60.0 = 20.0 * 3

    #: L6
    regular_nickels_value = regular_nickels * regular_nickel_value # eval: 3.5 = 70.0 * 0.05

    #: L7
    total_value = iron_nickels_value + regular_nickels_value # eval: 63.5 = 60.0 + 3.5

    #: FA
    answer = total_value
    return answer # eval: return 63.5
