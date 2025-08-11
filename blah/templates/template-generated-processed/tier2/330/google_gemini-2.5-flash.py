def solve():
    """Index: 330.
    Returns: the number of people who will go to the wedding.
    """
    # L1
    total_percentage = 100 # WK
    no_show_percentage = 5 # 5% typically don't show
    expected_show_percentage = total_percentage - no_show_percentage

    # L2
    total_expected_attendees = 220 # 220 people
    show_up_decimal_factor = 0.95 # from solution text: 0.95 (derived from 5% typically don't show)
    actual_attendees = total_expected_attendees * show_up_decimal_factor

    # FA
    answer = actual_attendees
    return answer