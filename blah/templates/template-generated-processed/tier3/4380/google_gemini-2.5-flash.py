def solve():
    """Index: 4380.
    Returns: the number of more photos Malachi took this year than last year.
    """
    # L1
    ratio_last_year = 10 # ratio of 10:17
    ratio_this_year = 17 # ratio of 10:17
    total_ratio_parts = ratio_last_year + ratio_this_year

    # L2
    ratio_difference = ratio_this_year - ratio_last_year

    # L3
    total_photos = 2430 # 2430 photos in his gallery
    more_photos_this_year = (ratio_difference / total_ratio_parts) * total_photos

    # FA
    answer = more_photos_this_year
    return answer