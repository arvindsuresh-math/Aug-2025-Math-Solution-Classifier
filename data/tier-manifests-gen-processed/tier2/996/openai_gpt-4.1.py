def solve():
    """Index: 996.
    Returns: the total amount James spent for the night.
    """
    # L1
    num_rounds = 2 # buys 2 rounds
    num_friends = 5 # for his 5 friends
    drinks_for_friends = num_rounds * num_friends

    # L2
    drinks_for_self = 6 # buys 6 drinks for himself
    total_drinks = drinks_for_friends + drinks_for_self

    # L3
    drink_cost = 6 # drinks cost $6 each
    total_drink_cost = total_drinks * drink_cost

    # L4
    food_cost = 14 # fried chicken costs $14
    order_total = total_drink_cost + food_cost

    # L5
    tip_percent = 0.3 # leaves a 30% tip
    tip_amount = order_total * tip_percent

    # L6
    order_with_tip = order_total + tip_amount

    # L7
    cover_charge = 20 # charges $20 to enter
    total_spent = order_with_tip + cover_charge

    # FA
    answer = total_spent
    return answer