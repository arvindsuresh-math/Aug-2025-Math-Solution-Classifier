def solve():
    """Index: 3865.
    Returns: the amount of money Faye had left.
    """
    # L1
    initial_money = 20 # Faye had $20
    mother_multiplier = 2 # twice as much
    money_from_mother = mother_multiplier * initial_money

    # L2
    total_money_before_spending = initial_money + money_from_mother

    # L3
    num_cupcakes = 10 # ten cupcakes
    cost_per_cupcake = 1.50 # $1.50 each
    total_cupcake_cost = num_cupcakes * cost_per_cupcake

    # L4
    num_cookie_boxes = 5 # five boxes of cookies
    cost_per_cookie_box = 3 # $3 per box
    total_cookie_cost = num_cookie_boxes * cost_per_cookie_box

    # L5
    total_spent = total_cupcake_cost + total_cookie_cost

    # L6
    money_left = total_money_before_spending - total_spent

    # FA
    answer = money_left
    return answer