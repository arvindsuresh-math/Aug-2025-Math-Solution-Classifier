def solve():
    """Index: 781.
    Returns: the total amount of money spent in the shop for all CDs.
    """
    # L1
    num_each_cd = 3 # bought 3 of each CD
    price_life_journey = 100 # CDs of The Life Journey for $100
    total_life_journey = num_each_cd * price_life_journey

    # L2
    price_rescind = 85 # When You Rescind for $85
    total_rescind = num_each_cd * price_rescind

    # L3
    price_day_life = 50 # A Day a Life for $50
    total_day_life = num_each_cd * price_day_life

    # L4
    total_cost = total_day_life + total_rescind + total_life_journey

    # FA
    answer = total_cost
    return answer