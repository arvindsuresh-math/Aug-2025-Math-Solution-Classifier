def solve():
    """Index: 1510.
    Returns: the number of junior girls on Ben's hockey team.
    """
    # L1
    percent_total = 100 # WK
    percent_boys = 60 # 60% boys
    percent_girls = percent_total - percent_boys

    # L2
    team_size = 50 # team has 50 players
    girls_fraction = percent_girls * 0.01 # convert percent to fraction
    num_girls = team_size * girls_fraction

    # L3
    girls_split = 2 # Half the girls are juniors
    num_junior_girls = num_girls / girls_split

    # FA
    answer = num_junior_girls
    return answer