def solve():
    """Index: 2388.
    Returns: the total amount Hank spent on apples and pears.
    """
    # L1
    dozens_apples = 14 # 14 dozen apples
    price_per_dozen_apples = 40 # apples cost 40 dollars for a dozen
    apples_cost = dozens_apples * price_per_dozen_apples

    # L2
    price_per_dozen_pears = 50 # pears cost 50 dollars for a dozen
    dozens_pears = 14 # 14 dozen pears
    pears_cost = price_per_dozen_pears * dozens_pears

    # L3
    total_cost = pears_cost + apples_cost

    # FA
    answer = total_cost
    return answer