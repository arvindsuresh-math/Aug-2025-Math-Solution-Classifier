def solve():
    """Index: 484.
    Returns: the number of people on the dance team now.
    """
    # L1
    initial_people = 25 # total of 25 people on their dance team
    people_quit = 8 # 8 people quit
    after_quit = initial_people - people_quit

    # L2
    new_people = 13 # 13 new people got in
    final_people = after_quit + new_people

    # FA
    answer = final_people
    return answer