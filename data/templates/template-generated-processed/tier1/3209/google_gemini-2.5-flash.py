def solve():
    """Index: 3209.
    Returns: the total yards run by the 3 athletes.
    """
    # L1
    malik_yards_per_game = 18 # 18 yards in each of 4 games
    num_games = 4 # in each of 4 games
    malik_total_yards = malik_yards_per_game * num_games

    # L2
    josiah_yards_per_game = 22 # 22 yards in each of 4 games
    josiah_total_yards = josiah_yards_per_game * num_games

    # L3
    darnell_yards_per_game = 11 # 11 yards rushed for each of the 4 games
    darnell_total_yards = darnell_yards_per_game * num_games

    # L4
    total_yards = malik_total_yards + josiah_total_yards + darnell_total_yards

    # FA
    answer = total_yards
    return answer