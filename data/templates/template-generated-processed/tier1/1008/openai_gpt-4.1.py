def solve():
    """Index: 1008.
    Returns: the number of muffins Lana still needs to sell to hit her goal.
    """
    # L1
    goal = 20 # Lana aims to sell 20 muffins at the bake sale
    sold_morning = 12 # She sells 12 muffins in the morning
    remaining_after_morning = goal - sold_morning

    # L2
    sold_afternoon = 4 # She sells another 4 in the afternoon
    muffins_left = remaining_after_morning - sold_afternoon

    # FA
    answer = muffins_left
    return answer