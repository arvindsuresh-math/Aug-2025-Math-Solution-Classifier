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
    nickels_per_quarter = value_quarter / value_nickel

    #: L2
    total_nickels = num_quarters * nickels_per_quarter

    #: L3
    num_iron_nickels = total_nickels * iron_nickel_percentage

    #: L4
    num_regular_nickels = total_nickels - num_iron_nickels

    #: L5
    value_iron_nickels = num_iron_nickels * value_iron_nickel

    #: L6
    value_regular_nickels = num_regular_nickels * value_nickel

    #: L7
    total_value = value_iron_nickels + value_regular_nickels

    answer = total_value # FINAL ANSWER
    return answer