def solve():
    """Index: 2731.
    Returns: the number of laps Jeff had remaining when he took the break on Sunday.
    """
    # L1
    total_laps = 98 # required him to swim 98 laps over the weekend
    saturday_laps = 27 # On Saturday, Jeff swam 27 laps
    after_saturday = total_laps - saturday_laps

    # L2
    sunday_morning_laps = 15 # On Sunday morning, he swam 15 laps
    after_sunday_morning = after_saturday - sunday_morning_laps

    # FA
    answer = after_sunday_morning
    return answer