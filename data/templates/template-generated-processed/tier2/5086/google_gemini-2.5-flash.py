def solve():
    """Index: 5086.
    Returns: the total money Trip could save by going to the earlier movie.
    """
    # L1
    evening_ticket_cost = 10 # An evening ticket cost $10
    food_combo_cost = 10 # a large popcorn & drink combo would cost him an additional $10
    total_evening_cost = evening_ticket_cost + food_combo_cost

    # L2
    ticket_discount_percent_text = 20 # save 20% off tickets
    ticket_discount_percent_decimal = 0.20 # save 20% off tickets
    ticket_discount_amount = evening_ticket_cost * ticket_discount_percent_decimal

    # L3
    food_discount_percent_text = 50 # 50% off any food combos
    food_discount_percent_decimal = 0.50 # 50% off any food combos
    food_discount_amount = food_combo_cost * food_discount_percent_decimal

    # L4
    total_savings = ticket_discount_amount + food_discount_amount

    # FA
    answer = total_savings
    return answer