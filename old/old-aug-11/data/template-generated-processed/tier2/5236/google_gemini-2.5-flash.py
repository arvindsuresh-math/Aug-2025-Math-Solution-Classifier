def solve():
    """Index: 5236.
    Returns: the total cost of the dog treats.
    """
    # L1
    treats_per_day = 2 # 2 treats a day
    days_in_month = 30 # month is 30 days long
    total_treats = treats_per_day * days_in_month

    # L2
    cost_per_treat = 0.1 # $.1 each
    total_cost = total_treats * cost_per_treat

    # FA
    answer = total_cost
    return answer