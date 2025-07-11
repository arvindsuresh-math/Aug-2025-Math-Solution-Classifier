def solve():
    """Index: 1149.
    Returns: the number of pages in the books Mandy reads now.
    """
    # L1
    initial_age = 6 # 6 years old
    multiplier_twice = 2 # twice that age
    age_at_twice = initial_age * multiplier_twice

    # L2
    initial_pages = 8 # only 8 pages
    multiplier_five_times = 5 # 5 times longer
    pages_at_twice_age = multiplier_five_times * initial_pages

    # L3
    years_later_first = 8 # 8 years later
    age_eight_years_later = age_at_twice + years_later_first

    # L4
    multiplier_three_times = 3 # 3 times longer than that
    pages_three_times_longer = multiplier_three_times * pages_at_twice_age

    # L5
    multiplier_four_times = 4 # 4 times the previous length
    current_pages = pages_three_times_longer * multiplier_four_times

    # FA
    answer = current_pages
    return answer