def solve(
        ken_amount: int = 1750, # Ken got $1750
        tony_multiplier: int = 2 # Tony got twice as much as Ken
    ):
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """
    #: L1
    tony_amount = tony_multiplier * ken_amount # eval: 3500 = 2 * 1750
    #: L2
    total_shared_money = ken_amount + tony_amount # eval: 5250 = 1750 + 3500
    answer = total_shared_money # FINAL ANSWER # eval: 5250 = 5250 # FINAL ANSWER
    return answer # eval: return 5250