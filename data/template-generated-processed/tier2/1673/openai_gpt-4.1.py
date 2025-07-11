def solve():
    """Index: 1673.
    Returns: how much more money Zachary needs.
    """
    # L1
    ball_cost = 3.75 # The ball costs $3.75
    shorts_cost = 2.40 # the shorts cost $2.40
    shoes_cost = 11.85 # the shoes cost $11.85
    total_cost = ball_cost + shorts_cost + shoes_cost

    # L2
    zachary_money = 10 # Zachary has $10
    money_needed = total_cost - zachary_money

    # FA
    answer = money_needed
    return answer