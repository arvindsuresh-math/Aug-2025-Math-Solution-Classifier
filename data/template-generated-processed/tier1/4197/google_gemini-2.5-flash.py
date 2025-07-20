def solve():
    """Index: 4197.
    Returns: the total money Chantal will gain from selling sweaters.
    """
    # L1
    num_sweaters = 28 # 28 sweaters
    yarn_balls_per_sweater = 4 # Each sweater takes 4 balls of yarn
    total_yarn_balls = num_sweaters * yarn_balls_per_sweater

    # L2
    cost_per_ball = 6 # Each ball of yarn costs $6
    total_yarn_cost = total_yarn_balls * cost_per_ball

    # L3
    sell_price_per_sweater = 35 # sells each sweater for $35
    total_earnings = sell_price_per_sweater * num_sweaters

    # L4
    total_gain = total_earnings - total_yarn_cost

    # FA
    answer = total_gain
    return answer