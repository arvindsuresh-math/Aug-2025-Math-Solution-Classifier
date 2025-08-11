def solve():
    """Index: 5966.
    Returns: the number of pages Xander has left to read.
    """
    # L1
    total_pages = 500 # 500-page book
    first_night_percent_num = 20 # 20%
    first_night_percent_decimal = 0.20 # 20% of his 500-page book in one hour
    percent_factor = 0.01 # WK
    pages_read_first_night = first_night_percent_decimal * total_pages

    # L2
    pages_left_after_first_night = total_pages - pages_read_first_night

    # L3
    second_night_percent_num = 20 # another 20%
    second_night_percent_decimal = 0.20 # another 20% of the book
    pages_read_second_night = second_night_percent_decimal * total_pages

    # L4
    pages_left_after_second_night = pages_left_after_first_night - pages_read_second_night

    # L5
    third_night_percent_num = 30 # 30%
    third_night_percent_decimal = 0.30 # 30% of his book
    pages_read_third_night = third_night_percent_decimal * total_pages

    # L6
    pages_left_final = pages_left_after_second_night - pages_read_third_night

    # FA
    answer = pages_left_final
    return answer