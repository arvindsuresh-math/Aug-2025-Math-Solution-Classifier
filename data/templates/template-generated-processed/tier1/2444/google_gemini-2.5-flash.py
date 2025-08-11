def solve():
    """Index: 2444.
    Returns: the amount needed to raise on the final day to reach the goal.
    """
    # L1
    num_bronze_families = 10 # 10 Bronze Status families
    bronze_donation_amount = 25 # donated $25
    bronze_total_collected = num_bronze_families * bronze_donation_amount

    # L2
    num_silver_families = 7 # 7 Silver Status Families
    silver_donation_amount = 50 # donated $50
    silver_total_collected = num_silver_families * silver_donation_amount

    # L3
    num_gold_families = 1 # 1 Gold Status family
    gold_donation_amount = 100 # donated $100
    gold_total_collected = num_gold_families * gold_donation_amount

    # L4
    total_collected_thus_far = bronze_total_collected + silver_total_collected + gold_total_collected

    # L5
    fundraiser_goal = 750 # collect $750
    amount_needed = fundraiser_goal - total_collected_thus_far

    # FA
    answer = amount_needed
    return answer