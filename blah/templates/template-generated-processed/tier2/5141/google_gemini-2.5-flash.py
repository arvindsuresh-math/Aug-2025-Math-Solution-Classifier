def solve():
    """Index: 5141.
    Returns: the entire price of the meal.
    """
    # L1
    num_people = 2 # Buffy and Oz
    entree_cost = 20.00 # Each of their entrees was $20.00
    total_entree_cost = num_people * entree_cost

    # L2
    appetizer_cost = 9.00 # an appetizer that cost $9.00
    dessert_cost = 11.00 # a dessert that was $11.00
    subtotal_cost = appetizer_cost + total_entree_cost + dessert_cost

    # L3
    tip_percent_num = 30 # 30% tip
    tip_percent_decimal = 0.30 # from solution text: 60*.30
    tip_amount = subtotal_cost * tip_percent_decimal

    # L4
    total_bill = subtotal_cost + tip_amount

    # FA
    answer = total_bill
    return answer