def solve():
    """Index: 5357.
    Returns: Tom's total score in the game.
    """
    # L1
    num_enemies_killed = 150 # killed 150 enemies
    points_per_enemy = 10 # 10 points for killing an enemy
    base_score = num_enemies_killed * points_per_enemy

    # L2
    bonus_percent_decimal = 0.5 # 50% bonus
    bonus_points = base_score * bonus_percent_decimal

    # L3
    total_score = base_score + bonus_points

    # FA
    answer = total_score
    return answer