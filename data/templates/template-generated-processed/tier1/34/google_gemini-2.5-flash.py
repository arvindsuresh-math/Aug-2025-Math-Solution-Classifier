def solve():
    """Index: 34.
    Returns: the total amount of money shared by Mr. Sam.
    """
    # L1
    ken_amount = 1750 # Ken got $1750
    multiplier_for_tony = 2 # Tony got twice as much as Ken
    tony_amount = multiplier_for_tony * ken_amount

    # L2
    total_shared_money = ken_amount + tony_amount

    # FA
    answer = total_shared_money
    return answer