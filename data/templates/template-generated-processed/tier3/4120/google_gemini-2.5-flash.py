def solve():
    """Index: 4120.
    Returns: the difference between Sam's count and the average count of shooting stars.
    """
    # L1
    bridget_stars = 14 # Bridget counted 14 shooting stars
    reginald_fewer = 2 # two fewer shooting stars
    reginald_stars = bridget_stars - reginald_fewer

    # L2
    sam_more = 4 # four more shooting stars
    sam_stars = reginald_stars + sam_more

    # L3
    number_of_people = 3 # for the three of them
    average_stars = (bridget_stars + reginald_stars + sam_stars) / number_of_people

    # L4
    sam_vs_average_difference = sam_stars - average_stars

    # FA
    answer = sam_vs_average_difference
    return answer