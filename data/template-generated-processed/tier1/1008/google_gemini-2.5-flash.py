def solve():
    """Index: 1008.
    Returns: the number of more muffins Lana needs to sell to hit her goal.
    """
    # L1
    total_goal = 20 # Lana aims to sell 20 muffins
    sold_morning = 12 # sells 12 muffins in the morning
    remaining_after_morning = total_goal - sold_morning

    # L2
    sold_afternoon = 4 # sells another 4 in the afternoon
    remaining_after_afternoon = remaining_after_morning - sold_afternoon

    # FA
    answer = remaining_after_afternoon
    return answer