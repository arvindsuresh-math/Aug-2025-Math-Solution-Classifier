def solve(
        ken_share: int = 1750, # Ken got $1750
        tony_multiplier: int = 2 # Tony got twice as much as Ken
    ):
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """
    #: L1
    tony_share = tony_multiplier * ken_share

    #: L2
    total_shared = ken_share + tony_share

    answer = total_shared # FINAL ANSWER
    return answer