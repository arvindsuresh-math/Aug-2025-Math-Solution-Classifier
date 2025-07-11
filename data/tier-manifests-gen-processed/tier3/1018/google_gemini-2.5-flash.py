def solve():
    """Index: 1018.
    Returns: the number of times Ron gets to pick a new book per year.
    """
    # L1
    num_couples = 3 # three couples
    people_per_couple = 2 # WK
    people_in_couples = num_couples * people_per_couple

    # L2
    num_single_people = 5 # five single people
    ron_and_wife = 2 # Ron and his wife
    total_members = people_in_couples + num_single_people + ron_and_wife

    # L3
    weeks_per_year = 52 # WK
    times_ron_picks = weeks_per_year / total_members

    # FA
    answer = times_ron_picks
    return answer