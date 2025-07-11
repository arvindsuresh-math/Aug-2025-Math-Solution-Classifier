def solve():
    """Index: 786.
    Returns: the number of reams of paper John needs to buy per year.
    """
    # L1
    stories_per_week = 3 # John writes 3 stories every week
    pages_per_short_story = 50 # Each short story is 50 pages
    pages_per_week_short_stories = stories_per_week * pages_per_short_story

    # L2
    weeks_per_year = 52 # WK
    pages_per_year_short_stories = pages_per_week_short_stories * weeks_per_year

    # L3
    pages_per_novel_year = 1200 # He also writes a novel that is 1200 pages each year
    total_pages_per_year = pages_per_year_short_stories + pages_per_novel_year

    # L4
    pages_per_sheet = 2 # Each sheet of paper can hold 2 pages
    sheets_per_year = total_pages_per_year / pages_per_sheet

    # L5
    sheets_per_ream = 500 # a ream contains 500 sheets
    reams_needed_per_year = sheets_per_year / sheets_per_ream

    # FA
    answer = reams_needed_per_year
    return answer