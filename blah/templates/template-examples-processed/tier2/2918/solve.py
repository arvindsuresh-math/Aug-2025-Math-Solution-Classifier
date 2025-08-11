def solve():
    """Index: 2918.
    Returns: the amount Monica will make from the party.
    """
    # L1
    num_guests = 20 # 20 guests
    cost_per_person = 25.00 # $25.00 per person
    base_cost = num_guests * cost_per_person

    # L2
    discount_percent_decimal = 0.10 # from solution text: .10*500
    discount_percent_num = 10 # 10% discount
    percent_factor = 0.01 # WK
    discount_amount = discount_percent_num * percent_factor * base_cost

    # L3
    final_cost = base_cost - discount_amount

    # FA
    answer = final_cost
    return answer