def solve(
    ken_amount: int = 1750, # If Ken got $1750
    tony_multiplier: int = 2 # Tony got twice as much as Ken
):
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """

    #: L1
    tony_amount = ken_amount * tony_multiplier # eval: 3500 = 1750 * 2

    #: L2
    total_shared = ken_amount + tony_amount # eval: 5250 = 1750 + 3500

    #: FA
    answer = total_shared # eval: 5250 = 5250
    return answer # eval: return 5250
