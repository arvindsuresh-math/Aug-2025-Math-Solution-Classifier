def solve():
    """Index: 2444.
    Returns: the amount the school needs to raise on the final day to reach their goal.
    """
    # L1
    num_bronze = 10 # 10 Bronze Status families
    bronze_amt = 25 # donate $25
    bronze_total = num_bronze * bronze_amt

    # L2
    num_silver = 7 # 7 Silver Status Families
    silver_amt = 50 # donate $50
    silver_total = num_silver * silver_amt

    # L3
    num_gold = 1 # 1 Gold Status family
    gold_amt = 100 # donate $100
    gold_total = num_gold * gold_amt

    # L4
    collected_so_far = bronze_total + silver_total + gold_total

    # L5
    goal = 750 # collect $750 for new basketball equipment
    amount_needed = goal - collected_so_far

    # FA
    answer = amount_needed
    return answer