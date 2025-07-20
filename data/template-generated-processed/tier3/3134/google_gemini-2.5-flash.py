def solve():
    """Index: 3134.
    Returns: the average steps Toby needs to walk on Friday and Saturday.
    """
    # L1
    average_daily_steps = 9000 # average of 9,000 steps per day
    days_in_week = 7 # WK
    total_steps_goal = days_in_week * average_daily_steps

    # L2
    sunday_steps = 9400 # On Sunday he walked 9,400 steps
    monday_steps = 9100 # On Monday he walked 9,100 steps
    tuesday_steps = 8300 # On Tuesday he walked 8,300 steps
    wednesday_steps = 9200 # On Wednesday he walked 9,200 steps
    thursday_steps = 8900 # On Thursday he walked 8,900 steps
    remaining_steps = total_steps_goal - sunday_steps - monday_steps - tuesday_steps - wednesday_steps - thursday_steps

    # L3
    remaining_days = 2 # Friday and Saturday
    average_steps_friday_saturday = remaining_steps / remaining_days

    # FA
    answer = average_steps_friday_saturday
    return answer