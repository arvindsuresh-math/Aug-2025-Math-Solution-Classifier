def solve():
    """Index: 4904.
    Returns: how many millions Star Wars earned.
    """
    # L1
    lion_king_earned_box_office = 200 # earned 200 million at the box office
    lion_king_cost_to_make = 10 # cost 10 million to make
    lion_king_profit = lion_king_earned_box_office - lion_king_cost_to_make

    # L2
    profit_multiplier = 2 # profit that was half of what Star Wars made
    star_wars_profit = lion_king_profit * profit_multiplier

    # L3
    star_wars_cost_to_make = 25 # Star Wars cost 25 million to make
    star_wars_earned = star_wars_cost_to_make + star_wars_profit

    # FA
    answer = star_wars_earned
    return answer