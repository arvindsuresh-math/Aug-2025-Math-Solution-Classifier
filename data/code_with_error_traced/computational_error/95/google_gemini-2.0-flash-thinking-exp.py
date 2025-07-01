def solve(
    num_quarters: int = 20, # Alice has 20 quarters
    percent_iron_nickels: float = 0.20, # 20% of the nickels are iron nickels
    value_iron_nickel: int = 3, # iron nickels worth $3 each
    value_quarter: float = 0.25, # (standard value of a quarter)
    value_nickel: float = 0.05 # (standard value of a nickel)
):
    """Index: 95.
    Returns: the total value of Alice's money after the exchange.
    """

    #: L1
    nickels_per_quarter = 6.0 # eval: 6.0 = 6.0

    #: L2
    total_nickels = num_quarters * nickels_per_quarter # eval: 120.0 = 20 * 6.0

    #: L3
    num_iron_nickels = total_nickels * percent_iron_nickels # eval: 24.0 = 120.0 * 0.2

    #: L4
    num_regular_nickels = total_nickels - num_iron_nickels # eval: 96.0 = 120.0 - 24.0

    #: L5
    value_of_iron_nickels = num_iron_nickels * value_iron_nickel # eval: 72.0 = 24.0 * 3

    #: L6
    value_of_regular_nickels = num_regular_nickels * value_nickel # eval: 4.800000000000001 = 96.0 * 0.05

    #: L7
    total_value = value_of_iron_nickels + value_of_regular_nickels # eval: 76.8 = 72.0 + 4.800000000000001

    #: FA
    answer = total_value
    return answer # eval: return 76.8
