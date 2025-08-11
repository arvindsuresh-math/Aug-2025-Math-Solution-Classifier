def solve():
    """Index: 6546.
    Returns: the number of people who ordered chicken.
    """
    # L1
    total_invited_people = 30 # invites 30 people
    no_show_percent_decimal = 0.2 # 20% didn't show up
    no_show_people = total_invited_people * no_show_percent_decimal

    # L2
    people_showed_up = total_invited_people - no_show_people

    # L3
    steak_percent_decimal = 0.75 # 75% of the people who show up get steak
    people_got_steak = people_showed_up * steak_percent_decimal

    # L4
    people_got_chicken = people_showed_up - people_got_steak

    # FA
    answer = people_got_chicken
    return answer