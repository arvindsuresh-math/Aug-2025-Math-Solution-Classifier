def solve():
    """Index: 4982.
    Returns: the total change they should have received.
    """
    # L1
    lee_money = 10 # Lee had $10
    friend_money = 8 # his friend had $8
    total_initial_money = lee_money + friend_money

    # L2
    chicken_wings_cost = 6 # chicken wings for $6
    chicken_salad_cost = 4 # chicken salad for $4
    soda_cost_per_item = 1 # 2 sodas for $1.00 each
    total_food_cost = chicken_wings_cost + chicken_salad_cost + soda_cost_per_item + soda_cost_per_item

    # L3
    tax_amount = 3 # The tax came to $3
    total_cost_with_tax = total_food_cost + tax_amount

    # L4
    change_received = total_initial_money - total_cost_with_tax

    # FA
    answer = change_received
    return answer