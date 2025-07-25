def solve():
    """Index: 1695.
    Returns: the number of games Tara's dad attended in her second year.
    """
    # L1
    games_played_per_year = 20 # Tara played 20 games each year
    attendance_percent_decimal = 0.9 # attended 90% of the games
    games_attended_first_year = games_played_per_year * attendance_percent_decimal

    # L2
    fewer_games_second_year = 4 # attended 4 fewer games
    games_attended_second_year = games_attended_first_year - fewer_games_second_year

    # FA
    answer = games_attended_second_year
    return answer