def solve():
    """Index: 4501.
    Returns: the total points Greendale high school has.
    """
    # L1
    first_game_points = 30 # scores 30 points in the first game
    half_divisor = 2 # half as much in the second game
    second_game_points = first_game_points / half_divisor

    # L2
    triple_multiplier = 3 # triple as much as the second game
    third_game_points = second_game_points * triple_multiplier

    # L3
    bonus_points = 50 # receives 50 bonus points
    roosevelt_total_points = first_game_points + second_game_points + third_game_points + bonus_points

    # L4
    greendale_less_points = 10 # 10 points less than Roosevelt high school
    greendale_total_points = roosevelt_total_points - greendale_less_points

    # FA
    answer = greendale_total_points
    return answer