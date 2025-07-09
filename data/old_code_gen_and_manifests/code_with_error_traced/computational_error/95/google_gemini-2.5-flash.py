def solve(
        num_quarters: int = 20, # Alice has 20 quarters
        iron_nickel_percentage: float = 0.20, # 20% of the nickels are iron nickels
        iron_nickel_value: int = 3 # iron nickels worth $3 each
    ):
    """Index: 95.
    Returns: the total value of Alice's money after exchanging quarters for nickels.
    """
    quarter_value = 0.25 # eval: 0.25 = 0.25
    nickel_value = 0.05 # eval: 0.05 = 0.05

    #: L1
    nickels_per_quarter = quarter_value / nickel_value # eval: 5.0 = 0.25 / 0.05

    #: L2
    total_nickels = num_quarters * nickels_per_quarter # eval: 100.0 = 20 * 5.0

    #: L3
    num_iron_nickels = total_nickels * iron_nickel_percentage # eval: 20.0 = 100.0 * 0.2

    #: L4
    num_regular_nickels = total_nickels - num_iron_nickels # eval: 80.0 = 100.0 - 20.0

    #: L5
    value_iron_nickels = num_iron_nickels * iron_nickel_value # eval: 60.0 = 20.0 * 3

    #: L6
    value_regular_nickels = num_regular_nickels * nickel_value # eval: 4.0 = 80.0 * 0.05

    #: L7
    total_value = 74.0 # eval: 74.0 = 74.0

    #: FA
    answer = total_value
    return answer # eval: return 74.0
