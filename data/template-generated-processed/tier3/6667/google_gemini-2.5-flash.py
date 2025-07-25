def solve():
    """Index: 6667.
    Returns: the total hours Rachel spent completing the essay.
    """
    # L1
    research_minutes = 45 # 45 minutes researching the topic
    editing_minutes = 75 # 75 minutes editing her essay
    researching_and_editing_minutes = research_minutes + editing_minutes

    # L2
    minutes_per_hour = 60 # WK
    researching_and_editing_hours = researching_and_editing_minutes / minutes_per_hour

    # L3
    pages_written = 6 # writes a total of 6 pages
    minutes_per_page = 30 # writes 1 page every 30 minutes
    writing_minutes = pages_written * minutes_per_page

    # L4
    writing_hours = writing_minutes / minutes_per_hour

    # L5
    total_hours = researching_and_editing_hours + writing_hours

    # FA
    answer = total_hours
    return answer