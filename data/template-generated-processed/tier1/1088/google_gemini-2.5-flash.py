def solve():
    """Index: 1088.
    Returns: the total number of cows in the ranch altogether.
    """
    # L1
    multiplier_three = 3 # three times the number of cows
    we_the_people_cows = 17 # We the People has 17 cows
    three_times_we_the_people = multiplier_three * we_the_people_cows

    # L2
    happy_good_healthy_family_more = 2 # two more than three times
    happy_good_healthy_family_cows = three_times_we_the_people + happy_good_healthy_family_more

    # L3
    total_cows = happy_good_healthy_family_cows + we_the_people_cows

    # FA
    answer = total_cows
    return answer