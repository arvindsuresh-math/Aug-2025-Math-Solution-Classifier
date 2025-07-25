def solve():
    """Index: 6379.
    Returns: the total number of pages Steve writes in a month.
    """
    # L1
    days_in_month = 30 # WK
    letter_frequency_days = 3 # every 3rd day
    normal_letters_count = days_in_month / letter_frequency_days

    # L2
    time_per_normal_letter = 20 # He spends 20 minutes writing the letters
    time_per_page_normal = 10 # It takes 10 minutes to write 1 page
    pages_per_normal_letter = time_per_normal_letter / time_per_page_normal

    # L3
    total_pages_normal_letters = pages_per_normal_letter * normal_letters_count

    # L4
    long_letter_time_multiplier = 2 # twice as long per page
    time_per_page_long_letter = long_letter_time_multiplier * time_per_page_normal

    # L5
    total_time_long_letter = 80 # he spends 80 minutes writing
    pages_long_letter = total_time_long_letter / time_per_page_long_letter

    # L6
    total_pages_month = total_pages_normal_letters + pages_long_letter

    # FA
    answer = total_pages_month
    return answer