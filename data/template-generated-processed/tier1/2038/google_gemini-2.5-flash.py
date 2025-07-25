def solve():
    """Index: 2038.
    Returns: the total time Joe spent cutting hair.
    """
    # L1
    num_women_hair = 3 # 3 women's
    time_per_woman_hair = 50 # 50 minutes to cut a woman's hair
    time_women_hair = num_women_hair * time_per_woman_hair

    # L2
    num_men_hair = 2 # 2 men's
    time_per_man_hair = 15 # 15 minutes to cut a man's hair
    time_men_hair = num_men_hair * time_per_man_hair

    # L3
    num_kids_hair = 3 # 3 children's hair
    time_per_kid_hair = 25 # 25 minutes to cut a kid's hair
    time_kids_hair = num_kids_hair * time_per_kid_hair

    # L4
    total_time = time_women_hair + time_men_hair + time_kids_hair

    # FA
    answer = total_time
    return answer