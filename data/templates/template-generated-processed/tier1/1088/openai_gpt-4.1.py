def solve():
    """Index: 1088.
    Returns: the total number of cows in the ranch altogether.
    """
    # L1
    cows_we_the_people = 17 # We the People has 17 cows
    multiplier = 3 # three times the number
    three_times_cows = multiplier * cows_we_the_people

    # L2
    extra_cows = 2 # two more than three times
    cows_happy_family = three_times_cows + extra_cows

    # L3
    total_cows = cows_happy_family + cows_we_the_people

    # FA
    answer = total_cows
    return answer