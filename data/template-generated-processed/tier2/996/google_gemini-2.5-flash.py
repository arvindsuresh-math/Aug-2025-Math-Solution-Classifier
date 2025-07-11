def solve():
    """Index: 996.
    Returns: the total amount James spent for the night.
    """
    # L1
    rounds_bought = 2 # 2 rounds
    friends_count = 5 # 5 friends
    drinks_for_friends = rounds_bought * friends_count

    # L2
    drinks_for_self = 6 # 6 drinks for himself
    total_drinks = drinks_for_friends + drinks_for_self

    # L3
    drink_cost_per_each = 6 # Drinks cost $6 each
    cost_of_drinks = total_drinks * drink_cost_per_each

    # L4
    fried_chicken_cost = 14 # fried chicken which costs $14
    cost_of_food_and_drinks = cost_of_drinks + fried_chicken_cost

    # L5
    tip_percent = 0.3 # 30% tip
    tip_amount = cost_of_food_and_drinks * tip_percent

    # L6
    total_order_cost_with_tip = cost_of_food_and_drinks + tip_amount

    # L7
    entry_charge = 20 # charges $20 to enter
    total_spent = total_order_cost_with_tip + entry_charge

    # FA
    answer = total_spent
    return answer