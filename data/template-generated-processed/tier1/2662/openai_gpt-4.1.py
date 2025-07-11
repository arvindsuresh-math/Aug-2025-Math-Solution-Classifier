def solve():
    """Index: 2662.
    Returns: the number of journal pages each student will write in 6 weeks.
    """
    # L1
    sessions_per_week = 3 # 3 journal-writing sessions per week
    pages_per_session = 4 # writes 4 pages in each session
    pages_per_week = sessions_per_week * pages_per_session

    # L2
    num_weeks = 6 # in 6 weeks
    total_pages = pages_per_week * num_weeks

    # FA
    answer = total_pages
    return answer