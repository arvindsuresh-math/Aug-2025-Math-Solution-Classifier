def solve():
    """Index: 484.
    Returns: the number of people now on the dance team.
    """
    # L1
    initial_team = 25 # total of 25 people on their dance team
    people_quit = 8 # 8 people quit
    after_quit = initial_team - people_quit

    # L2
    people_joined = 13 # 13 new people got in
    after_joined = after_quit + people_joined

    # FA
    answer = after_joined
    return answer