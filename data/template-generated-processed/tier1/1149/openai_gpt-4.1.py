def solve():
    """Index: 1149.
    Returns: the number of pages in the books Mandy reads now.
    """
    # L1
    starting_age = 6 # when she was 6 years old
    twice = 2 # twice that age
    age_at_twice = starting_age * twice

    # L2
    starting_pages = 8 # books with only 8 pages
    five_times = 5 # 5 times longer
    pages_at_twice_age = five_times * starting_pages

    # L3
    years_later = 8 # 8 years later
    age_after_years = age_at_twice + years_later

    # L4
    three_times = 3 # 3 times longer than that
    pages_after_years = three_times * pages_at_twice_age

    # L5
    four_times = 4 # 4 times the previous length
    pages_present = pages_after_years * four_times

    # FA
    answer = pages_present
    return answer