def solve():
    """Index: 34.
    Returns: the total amount of money shared between Ken and Tony.
    """
    # L1
    ken_amount = 1750 # Ken got $1750
    tony_multiplier = 2 # Tony got twice as much as Ken
    tony_amount = tony_multiplier * ken_amount

    # L2
    total_shared = ken_amount + tony_amount

    # FA
    answer = total_shared
    return answer