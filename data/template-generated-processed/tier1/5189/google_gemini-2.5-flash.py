def solve():
    """Index: 5189.
    Returns: the total time it took the team to finish the race.
    """
    # L1
    jen_time = 30 # Jen ran third and finished in 30 seconds
    susan_longer_than_jen = 10 # Susan took 10 seconds longer than Jen
    susan_time = jen_time + susan_longer_than_jen

    # L2
    mary_multiplier_susan = 2 # Mary took twice as long as Susan
    mary_time = susan_time * mary_multiplier_susan

    # L3
    tiffany_less_than_mary = 7 # Tiffany finished in 7 seconds less than Mary
    tiffany_time = mary_time - tiffany_less_than_mary

    # L4
    total_team_time = mary_time + susan_time + jen_time + tiffany_time

    # FA
    answer = total_team_time
    return answer