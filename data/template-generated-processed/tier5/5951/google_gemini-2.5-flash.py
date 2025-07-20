def solve():
    """Index: 5951.
    Returns: the number of pages Cora has to read on Thursday.
    """
    # L3
    pages_monday = 23 # read 23 pages on Monday
    pages_tuesday = 38 # 38 pages on Tuesday
    pages_wednesday = 61 # 61 pages on Wednesday
    total_pages_book = 158 # a 158-page book
    multiplier_friday = 2 # twice as much on Friday as she does on Thursday
    coefficient_P = 1 # WK
    combined_coefficient_P = coefficient_P + multiplier_friday
    pages_remaining_for_thursday_friday = total_pages_book - pages_monday - pages_tuesday - pages_wednesday

    # L5
    pages_on_thursday = pages_remaining_for_thursday_friday / combined_coefficient_P

    # FA
    answer = pages_on_thursday
    return answer