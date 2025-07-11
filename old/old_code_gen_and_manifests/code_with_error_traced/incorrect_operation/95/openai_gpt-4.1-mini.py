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
    iron_nickels = total_nickels - iron_nickel_fraction # eval: 99.8 = 100.0 - 0.2

    #: L4
    regular_nickels = total_nickels - iron_nickels # eval: 0.20000000000000284 = 100.0 - 99.8

    #: L5
    iron_nickels_value = iron_nickels * iron_nickel_value # eval: 299.4 = 99.8 * 3

    #: L6
    regular_nickels_value = regular_nickels * regular_nickel_value # eval: 0.010000000000000142 = 0.20000000000000284 * 0.05

    #: L7
    total_value = iron_nickels_value + regular_nickels_value # eval: 299.40999999999997 = 299.4 + 0.010000000000000142

    #: FA
    answer = total_value
    return answer # eval: return 299.40999999999997
