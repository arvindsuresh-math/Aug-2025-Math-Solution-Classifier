def solve():
    """Index: 2317.
    Returns: the final bill total.
    """
    # L1
    num_twins = 2 # twin boys
    cheeseburger_cost_each = 13.50 # $13.50 each
    total_cheeseburger_cost = num_twins * cheeseburger_cost_each

    # L2
    num_people = 4 # party for 4 people
    dessert_cost_each = 6.00 # $6.00 each
    total_dessert_cost = num_people * dessert_cost_each

    # L3
    mom_lobster_cost = 25.50 # lobster for $25.50
    dad_steak_cost = 35.00 # steak for $35.00
    appetizer_cost = 8.50 # appetizer that cost 8.50
    subtotal_meals = mom_lobster_cost + dad_steak_cost + total_cheeseburger_cost + appetizer_cost + total_dessert_cost

    # L4
    tip_percent_num = 20 # 20% tip
    tip_percent_decimal = 0.20 # from solution text: .20*120.00
    percent_factor = 0.01 # WK
    tip_amount = tip_percent_num * percent_factor * subtotal_meals

    # L5
    final_bill_total = subtotal_meals + tip_amount

    # FA
    answer = final_bill_total
    return answer