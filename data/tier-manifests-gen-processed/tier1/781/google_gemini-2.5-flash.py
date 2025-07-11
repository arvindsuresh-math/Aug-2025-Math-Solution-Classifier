def solve():
    """Index: 781.
    Returns: the total amount of money spent in the shop.
    """
    # L1
    num_cds_bought = 3 # bought 3 of each CD
    cost_life_journey_per_cd = 100 # CDs of The Life Journey for $100
    total_cost_life_journey = num_cds_bought * cost_life_journey_per_cd

    # L2
    cost_when_you_rescind_per_cd = 85 # When You Rescind for $85
    total_cost_when_you_rescind = num_cds_bought * cost_when_you_rescind_per_cd

    # L3
    cost_a_day_a_life_per_cd = 50 # A Day a Life for $50
    total_cost_a_day_a_life = num_cds_bought * cost_a_day_a_life_per_cd

    # L4
    total_cost_all_cds = total_cost_a_day_a_life + total_cost_when_you_rescind + total_cost_life_journey

    # FA
    answer = total_cost_all_cds
    return answer