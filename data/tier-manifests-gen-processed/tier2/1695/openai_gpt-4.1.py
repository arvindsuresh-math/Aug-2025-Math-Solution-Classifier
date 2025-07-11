def solve():
    """Index: 1695.
    Returns: the number of games Tara's dad attended in her second year playing soccer.
    """
    # L1
    games_per_year = 20 # Tara played 20 games each year
    attendance_percent = 0.9 # attended 90% of the games
    first_year_attended = games_per_year * attendance_percent

    # L2
    games_fewer = 4 # attended 4 fewer games in second year
    second_year_attended = first_year_attended - games_fewer

    # FA
    answer = second_year_attended
    return answer