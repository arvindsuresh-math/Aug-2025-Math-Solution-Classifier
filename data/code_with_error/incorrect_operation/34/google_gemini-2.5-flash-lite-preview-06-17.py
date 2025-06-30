def solve(
    ken_amount: int = 1750, # If Ken got $1750
    tony_multiplier: int = 2 # Tony got twice as much as Ken
):
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """

    #: L1
    tony_amount = ken_amount * tony_multiplier

    #: L2
    total_shared = ken_amount - tony_amount

    #: FA
    answer = total_shared
    return answer