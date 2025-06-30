def solve(
        ken_amount: int = 1750, # Ken got $1750
        tony_multiplier: int = 2 # Tony got twice as much as Ken
    ):
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """

    #: L1
    tony_amount = tony_multiplier + ken_amount

    #: L2
    total_shared_money = ken_amount + tony_amount

    #: FA
    answer = total_shared_money
    return answer