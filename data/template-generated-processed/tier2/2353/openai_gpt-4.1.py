def solve():
    """Index: 2353.
    Returns: the total amount Bret spends on dinner.
    """
    # L1
    num_people = 4 # Bret and a team of 3 co-workers (so 4 people)
    main_meal_cost = 12.0 # Each main meal costs $12.0
    total_main_meal_cost = num_people * main_meal_cost

    # L2
    num_appetizers = 2 # 2 appetizers
    appetizer_cost = 6.0 # $6.00 each
    total_appetizer_cost = num_appetizers * appetizer_cost

    # L3
    subtotal = total_main_meal_cost + total_appetizer_cost

    # L4
    tip_percent = 0.20 # 20% tip
    tip_amount = tip_percent * subtotal

    # L5
    rush_fee = 5.00 # extra $5.00 to make it a rush order
    total_cost = subtotal + tip_amount + rush_fee

    # FA
    answer = total_cost
    return answer