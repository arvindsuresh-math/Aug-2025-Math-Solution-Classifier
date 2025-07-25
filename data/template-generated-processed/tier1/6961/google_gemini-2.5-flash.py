def solve():
    """Index: 6961.
    Returns: the number of bottles of water used during the second game.
    """
    # L1
    num_cases = 10 # 10 cases of bottled water
    bottles_per_case = 20 # 20 bottles in each case
    total_initial_bottles = num_cases * bottles_per_case

    # L2
    bottles_used_first_game = 70 # Seventy bottles of water were used during the first game
    bottles_after_first_game = total_initial_bottles - bottles_used_first_game

    # L3
    bottles_left_after_second_game = 20 # only 20 bottles of water were left
    bottles_used_second_game = bottles_after_first_game - bottles_left_after_second_game

    # FA
    answer = bottles_used_second_game
    return answer