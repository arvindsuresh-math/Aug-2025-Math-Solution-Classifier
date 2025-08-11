def solve():
    """Index: 330.
    Returns: the expected number of people who will go to Laura's wedding.
    """
    # L1
    total_percent = 100 # WK: percent is out of 100
    percent_no_show = 5 # approximately 5% typically don't show
    percent_show = total_percent - percent_no_show
    
    # L2
    expected_guests = 220 # Laura expects 220 people to attend
    percent_show_decimal = 0.95 # 95% as decimal
    expected_attendance = expected_guests * percent_show_decimal
    
    # FA
    answer = expected_attendance
    return answer