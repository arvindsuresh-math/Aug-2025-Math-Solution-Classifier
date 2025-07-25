def solve():
    """Index: 2353.
    Returns: the total amount Bret spends on dinner.
    """
    # L1
    num_coworkers = 4 # Bret and a team of 3 co-workers
    meal_cost_per_person = 12.0 # Each main meal costs $12.0
    total_meal_cost = num_coworkers * meal_cost_per_person

    # L2
    num_appetizers = 2 # 2 appetizers
    appetizer_cost_each = 6.00 # $6.00 each
    total_appetizer_cost = num_appetizers * appetizer_cost_each

    # L3
    subtotal_cost = total_meal_cost + total_appetizer_cost

    # L4
    tip_percent_num = 20 # 20% tip
    tip_percent_decimal = 0.20 # 20% tip
    tip_amount = tip_percent_decimal * subtotal_cost

    # L5
    rush_order_fee = 5.00 # an extra $5.00
    total_spend = subtotal_cost + tip_amount + rush_order_fee

    # FA
    answer = total_spend
    return answer