def solve():
    """Index: 2052.
    Returns: the total number of days Jane spent reading the book.
    """
    # L1
    total_pages = 500 # 500 page book
    half_divisor = 2 # Half of the book
    half_pages = total_pages / half_divisor

    # L2
    speed_first_half = 10 # speed of 10 pages per day
    days_first_half = half_pages / speed_first_half

    # L3
    speed_second_half = 5 # speed of 5 pages a day
    days_second_half = half_pages / speed_second_half

    # L4
    total_days = days_first_half + days_second_half

    # FA
    answer = total_days
    return answer