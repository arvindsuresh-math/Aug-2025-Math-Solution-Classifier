def solve():
    """Index: 4460.
    Returns: the amount saved with his vest.
    """
    # L1
    weight_plates_pounds = 200 # 200 pounds of weight plates
    cost_per_pound = 1.2 # $1.2 per pound
    weight_plates_cost = weight_plates_pounds * cost_per_pound

    # L2
    vest_cost = 250 # weight vest for $250
    total_cost_his_vest = vest_cost + weight_plates_cost

    # L3
    other_vest_full_cost = 700 # A 200-pound weight vest would cost $700
    discount_other_vest = 100 # a $100 discount
    other_vest_discounted_cost = other_vest_full_cost - discount_other_vest

    # L4
    amount_saved = other_vest_discounted_cost - total_cost_his_vest

    # FA
    answer = amount_saved
    return answer