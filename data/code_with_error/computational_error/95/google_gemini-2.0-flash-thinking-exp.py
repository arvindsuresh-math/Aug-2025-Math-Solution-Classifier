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
    nickels_per_quarter = 6.0

    #: L2
    total_nickels = num_quarters * nickels_per_quarter

    #: L3
    num_iron_nickels = total_nickels * percent_iron_nickels

    #: L4
    num_regular_nickels = total_nickels - num_iron_nickels

    #: L5
    value_of_iron_nickels = num_iron_nickels * value_iron_nickel

    #: L6
    value_of_regular_nickels = num_regular_nickels * value_nickel

    #: L7
    total_value = value_of_iron_nickels + value_of_regular_nickels

    #: FA
    answer = total_value
    return answer