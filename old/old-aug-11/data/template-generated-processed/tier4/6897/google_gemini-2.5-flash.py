def solve():
    """Index: 6897.
    Returns: the number of minutes Mike can play at the arcade.
    """
    # L1
    weekly_pay = 100 # 100 dollars a week
    arcade_spend_fraction = 0.5 # half of that at an arcade
    spent_at_arcade = weekly_pay * arcade_spend_fraction

    # L2
    food_cost = 10 # spends 10 dollars at the arcade on food
    spent_on_tokens = spent_at_arcade - food_cost

    # L3
    cost_per_hour = 8 # 1 hour for $8
    playable_hours = spent_on_tokens / cost_per_hour

    # L4
    minutes_per_hour = 60 # WK
    playable_minutes = playable_hours * minutes_per_hour

    # FA
    answer = playable_minutes
    return answer