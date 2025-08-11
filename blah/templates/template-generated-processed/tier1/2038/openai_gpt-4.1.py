def solve():
    """Index: 2038.
    Returns: the total time Joe spent cutting hair in minutes.
    """
    # L1
    num_women = 3 # 3 women's hair
    time_per_woman = 50 # 50 minutes to cut a woman's hair
    women_time = num_women * time_per_woman

    # L2
    num_men = 2 # 2 men's hair
    time_per_man = 15 # 15 minutes to cut a man's hair
    men_time = num_men * time_per_man

    # L3
    num_kids = 3 # 3 children's hair
    time_per_kid = 25 # 25 minutes to cut a kid's hair
    kids_time = num_kids * time_per_kid

    # L4
    total_time = women_time + men_time + kids_time

    # FA
    answer = total_time
    return answer