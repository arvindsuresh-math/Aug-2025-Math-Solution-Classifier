def solve():
    """Index: 2728.
    Returns: the amount of money the farmer would lose.
    """
    # L1
    total_initial_cattle = 340 # 340 head of cattle
    total_original_price = 204000 # $204,000
    original_price_per_head = total_original_price / total_initial_cattle

    # L2
    sick_cattle_died = 172 # 172 of them fell sick and died
    remaining_cattle = total_initial_cattle - sick_cattle_died

    # L3
    price_reduction_per_head = 150 # lower his price by $150 per head
    lowered_price_per_head = original_price_per_head - price_reduction_per_head

    # L4
    money_at_lowered_price = lowered_price_per_head * remaining_cattle

    # L5
    money_at_original_price_remaining_cattle = original_price_per_head * remaining_cattle

    # L6
    money_lost = money_at_original_price_remaining_cattle - money_at_lowered_price

    # FA
    answer = money_lost
    return answer