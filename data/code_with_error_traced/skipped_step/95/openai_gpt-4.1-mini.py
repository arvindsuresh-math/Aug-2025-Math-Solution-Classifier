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

    #: L2
    total_nickels = num_quarters * regular_nickel_value # eval: 1.0 = 20 * 0.05

    #: L3
    iron_nickels = total_nickels * iron_nickel_fraction # eval: 0.2 = 1.0 * 0.2

    #: L4
    regular_nickels = total_nickels - iron_nickels # eval: 0.8 = 1.0 - 0.2

    #: L5
    iron_nickels_value = iron_nickels * iron_nickel_value # eval: 0.6000000000000001 = 0.2 * 3

    #: L6
    regular_nickels_value = regular_nickels * regular_nickel_value # eval: 0.04000000000000001 = 0.8 * 0.05

    #: L7
    total_value = iron_nickels_value + regular_nickels_value # eval: 0.6400000000000001 = 0.6000000000000001 + 0.04000000000000001

    #: FA
    answer = total_value
    return answer # eval: return 0.6400000000000001
