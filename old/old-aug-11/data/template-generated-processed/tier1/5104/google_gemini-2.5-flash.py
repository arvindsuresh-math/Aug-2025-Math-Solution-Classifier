def solve():
    """Index: 5104.
    Returns: the total number of seats needed on the bus.
    """
    # L1
    trumpet_multiplier = 3 # three times as many members who play the trumpet
    flute_members = 5 # Five members play the flute
    trumpet_players = trumpet_multiplier * flute_members

    # L2
    fewer_trombone_than_trumpet = 8 # eight fewer trombone players than trumpeters
    trombone_players = trumpet_players - fewer_trombone_than_trumpet

    # L3
    more_drummers_than_trombone = 11 # eleven more drummers than trombone players
    drummers = trombone_players + more_drummers_than_trombone

    # L4
    clarinet_multiplier = 2 # twice as many members that play the clarinet as members that play the flute
    clarinet_players = clarinet_multiplier * flute_members

    # L5
    more_french_horn_than_trombone = 3 # Three more members play the French horn than play the trombone
    french_horn_players = trombone_players + more_french_horn_than_trombone

    # L6
    total_seats_needed = flute_members + trumpet_players + trombone_players + drummers + clarinet_players + french_horn_players

    # FA
    answer = total_seats_needed
    return answer