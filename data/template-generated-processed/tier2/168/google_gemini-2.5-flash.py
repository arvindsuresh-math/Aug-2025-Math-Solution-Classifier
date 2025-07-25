def solve():
    """Index: 168.
    Returns: the total cost of Silvia's order with the discount.
    """
    # L1
    num_quiches = 2 # 2 quiches
    cost_per_quiche = 15.00 # $15.00 each
    cost_quiches = num_quiches * cost_per_quiche

    # L2
    num_croissants = 6 # 6 croissants
    cost_per_croissant_from_question = 3.00 # $3.00 each
    cost_per_croissant_from_solution_text = 2.5 # from solution text: 6*2.5
    cost_per_croissant_from_solution_calc = 3 # from solution text: <<6*3=18.00>>
    cost_croissants = num_croissants * cost_per_croissant_from_solution_calc

    # L3
    num_biscuits = 6 # 6 buttermilk biscuits
    cost_per_biscuit = 2.00 # $2.00 each
    cost_biscuits = num_biscuits * cost_per_biscuit

    # L4
    total_pre_discount_cost = cost_quiches + cost_croissants + cost_biscuits

    # L5
    discount_threshold = 50.00 # over $50.00
    discount_percent_text = 10 # 10% on advanced orders
    discount_percent_decimal = 0.10 # from solution text: .10*60
    discount_amount = discount_percent_decimal * total_pre_discount_cost

    # L6
    final_cost = total_pre_discount_cost - discount_amount

    # FA
    answer = final_cost
    return answer