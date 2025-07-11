def solve():
    """Index: 1681.
    Returns: the total amount Jake spends on car soap.
    """
    # L1
    total_washes = 20 # he washes his car once a week for 20 weeks
    washes_per_bottle = 4 # 1 bottle of car wash soap 4 times
    bottles_needed = total_washes / washes_per_bottle

    # L2
    cost_per_bottle = 4 # Each bottle costs $4.00
    total_cost = cost_per_bottle * bottles_needed

    # FA
    answer = total_cost
    return answer