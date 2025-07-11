def solve():
    """Index: 960.
    Returns: Greg's age.
    """
    # L1
    cindy_age = 5 # Cindy was 5 years old
    jan_older_than_cindy = 2 # Jan was 2 years older than Cindy
    jan_age = jan_older_than_cindy + cindy_age

    # L2
    marcia_multiplier = 2 # twice as old as Jan
    marcia_age = marcia_multiplier * jan_age

    # L3
    greg_older_than_marcia = 2 # Greg was two years older than Marcia
    greg_age = greg_older_than_marcia + marcia_age

    # FA
    answer = greg_age
    return answer