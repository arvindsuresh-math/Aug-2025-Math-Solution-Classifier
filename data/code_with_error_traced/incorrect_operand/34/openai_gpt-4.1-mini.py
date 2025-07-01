def solve(
    ken_amount: int = 1750  # Ken got $1750
):
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """

    #: L1
    tony_amount = 2 * ken_amount # eval: 3500 = 2 * 1750

    #: L2
    total_shared = ken_amount + ken_amount # eval: 3500 = 1750 + 1750

    #: FA
    answer = total_shared
    return answer # eval: return 3500
