def solve():
    """Index: 1364.
    Returns: the total amount Gina will spend on college.
    """
    # L1
    num_credits = 14 # 14 credits
    cost_per_credit = 450 # $450 each
    tuition_cost = num_credits * cost_per_credit

    # L2
    num_textbooks = 5 # 5 textbooks
    cost_per_textbook = 120 # $120 for each of her 5 textbooks
    textbooks_cost = num_textbooks * cost_per_textbook

    # L3
    facilities_fee = 200 # a $200 facilities fee
    total_cost = tuition_cost + textbooks_cost + facilities_fee

    # FA
    answer = total_cost
    return answer