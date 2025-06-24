def solve_3():
    # Total pages in the book
    total_pages = 120

    # Pages read yesterday
    pages_read_yesterday = 12

    # Pages read today (twice as many as yesterday)
    pages_read_today = pages_read_yesterday * 2

    # Total pages read so far
    total_pages_read = pages_read_yesterday + pages_read_today

    # Remaining pages to be read
    remaining_pages = total_pages - total_pages_read

    # Pages Julie wants to read tomorrow (half of the remaining pages)
    pages_to_read_tomorrow = remaining_pages / 2

    return int(pages_to_read_tomorrow)