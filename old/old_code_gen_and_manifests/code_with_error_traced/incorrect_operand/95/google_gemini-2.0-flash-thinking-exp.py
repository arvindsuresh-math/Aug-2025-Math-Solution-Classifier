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
    nickels_per_quarter = value_quarter / value_nickel # eval: 5.0 = 0.25 / 0.05

    #: L2
    total_nickels = value_nickel * nickels_per_quarter # eval: 0.25 = 0.05 * 5.0

    #: L3
    num_iron_nickels = total_nickels * percent_iron_nickels # eval: 0.05 = 0.25 * 0.2

    #: L4
    num_regular_nickels = total_nickels - num_iron_nickels # eval: 0.2 = 0.25 - 0.05

    #: L5
    value_of_iron_nickels = num_iron_nickels * value_iron_nickel # eval: 0.15000000000000002 = 0.05 * 3

    #: L6
    value_of_regular_nickels = num_regular_nickels * value_nickel # eval: 0.010000000000000002 = 0.2 * 0.05

    #: L7
    total_value = value_of_iron_nickels + value_of_regular_nickels # eval: 0.16000000000000003 = 0.15000000000000002 + 0.010000000000000002

    #: FA
    answer = total_value
    return answer # eval: return 0.16000000000000003
