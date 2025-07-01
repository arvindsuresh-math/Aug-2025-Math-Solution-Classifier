def solve(
    num_quarters: int = 20, # Alice has 20 quarters
    value_quarter: float = 0.25, # A quarter is worth $0.25
    value_nickel: float = 0.05, # A nickel is worth $0.05
    iron_nickel_percentage: float = 0.20, # 20% of the nickels are iron nickels
    value_iron_nickel: int = 3 # iron nickels worth $3 each
):
    """Index: 95.
    Returns: the total value of her money after the exchange.
    """

    #: L1

    #: L2
    total_nickels = num_quarters * iron_nickel_percentage # eval: 4.0 = 20 * 0.2

    #: L3
    num_iron_nickels = total_nickels * iron_nickel_percentage # eval: 0.8 = 4.0 * 0.2

    #: L4
    num_regular_nickels = total_nickels - num_iron_nickels # eval: 3.2 = 4.0 - 0.8

    #: L5
    value_iron_nickels = num_iron_nickels * value_iron_nickel # eval: 2.4000000000000004 = 0.8 * 3

    #: L6
    value_regular_nickels = num_regular_nickels * value_nickel # eval: 0.16000000000000003 = 3.2 * 0.05

    #: L7
    total_value = value_iron_nickels + value_regular_nickels # eval: 2.5600000000000005 = 2.4000000000000004 + 0.16000000000000003

    #: FA
    answer = total_value
    return answer # eval: return 2.5600000000000005
