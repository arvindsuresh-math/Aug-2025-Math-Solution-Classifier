def solve():
    """Index: 526.
    Returns: the total number of pages Mack writes from Monday to Wednesday.
    """
    # L1
    monday_minutes = 60 # Mack writes in his journal for 60 minutes (Monday)
    monday_minutes_per_page = 30 # 1 page every 30 minutes (Monday)
    monday_pages = monday_minutes / monday_minutes_per_page

    # L2
    tuesday_minutes = 45 # Mack writes in his journal for 45 minutes (Tuesday)
    tuesday_minutes_per_page = 15 # 1 page every 15 minutes (Tuesday)
    tuesday_pages = tuesday_minutes / tuesday_minutes_per_page

    # L3
    wednesday_pages = 5 # Mack writes 5 pages in his journal (Wednesday)
    total_pages = monday_pages + tuesday_pages + wednesday_pages

    # FA
    answer = total_pages
    return answer