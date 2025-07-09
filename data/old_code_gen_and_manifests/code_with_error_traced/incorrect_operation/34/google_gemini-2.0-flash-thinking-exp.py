def solve(
    ken_amount: int = 1750 # Ken got $1750
):
    """Index: 34.
    Returns: the total amount of money shared.
    """

    #: L1
    tony_amount = 2 - ken_amount # eval: -1748 = 2 - 1750

    #: L2
    total_shared = ken_amount + tony_amount # eval: 2 = 1750 + -1748

    #: FA
    answer = total_shared
    return answer # eval: return 2
