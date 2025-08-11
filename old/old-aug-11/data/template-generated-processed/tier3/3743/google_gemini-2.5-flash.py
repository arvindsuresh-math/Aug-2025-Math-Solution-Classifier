def solve():
    """Index: 3743.
    Returns: the amount Calum can afford to spend on each disco ball.
    """
    # L1
    num_food_boxes = 10 # 10 boxes of food
    cost_per_food_box = 25 # Each box of food costs $25
    total_food_cost = num_food_boxes * cost_per_food_box

    # L2
    total_budget = 330 # Calum
    remaining_budget_for_disco_balls = total_budget - total_food_cost

    # L3
    num_disco_balls = 4 # 4 disco balls
    cost_per_disco_ball = remaining_budget_for_disco_balls / num_disco_balls

    # FA
    answer = cost_per_disco_ball
    return answer