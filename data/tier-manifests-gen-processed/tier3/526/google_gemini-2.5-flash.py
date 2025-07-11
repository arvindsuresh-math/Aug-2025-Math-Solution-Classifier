def solve():
    """Index: 526.
    Returns: the total number of pages Mack writes in his journal.
    """
    # L1
    monday_writing_minutes = 60 # 60 minutes
    monday_rate_minutes_per_page = 30 # 1 page every 30 minutes
    monday_pages = monday_writing_minutes / monday_rate_minutes_per_page

    # L2
    tuesday_writing_minutes = 45 # 45 minutes
    tuesday_rate_minutes_per_page = 15 # 1 page every 15 minutes
    tuesday_pages = tuesday_writing_minutes / tuesday_rate_minutes_per_page

    # L3
    wednesday_pages = 5 # Mack writes 5 pages
    total_pages = monday_pages + tuesday_pages + wednesday_pages

    # FA
    answer = total_pages
    return answer