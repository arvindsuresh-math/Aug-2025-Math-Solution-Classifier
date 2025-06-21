import math

def solve(
        num_chapters: int = 2, # 2 chapters of their textbook
        num_worksheets: int = 4, # 4 worksheets to memorize
        hours_per_chapter: int = 3, # dedicate 3 hours to each chapter of their textbook
        hours_per_worksheet: float = 1.5, # 1.5 hours for each worksheet
        max_hours_per_day: int = 4, # no more than 4 hours each day
        break_minutes_per_hour: int = 10, # take a 10-minute break every hour
        num_snack_breaks: int = 3, # include 3 10-minute snack breaks
        minutes_per_snack_break: int = 10, # 10-minute snack breaks
        lunch_minutes_per_day: int = 30 # 30 minutes for lunch each day
    ):
    """Index: 7364.
    Returns: the total number of days Angelo and Melanie should plan to study.
    """
    #: L1
    total_hours_chapters = hours_per_chapter * num_chapters

    #: L2
    total_hours_worksheets = hours_per_worksheet * num_worksheets

    #: L3
    total_study_hours_no_breaks = total_hours_chapters + total_hours_worksheets
    # The solution calculates initial_study_days here, but it's not the final answer,
    # and the break calculations depend on total_study_hours_no_breaks.
    # So, we calculate it here and use it later.

    #: L4
    break_minutes_from_study = total_study_hours_no_breaks * break_minutes_per_hour

    #: L5
    total_snack_break_minutes = num_snack_breaks * minutes_per_snack_break

    #: L6
    # The solution implies these are total minutes for the entire study period, not per day.
    total_break_minutes = break_minutes_from_study + total_snack_break_minutes + lunch_minutes_per_day
    total_break_hours = total_break_minutes / 60

    #: L7
    grand_total_hours = total_study_hours_no_breaks + total_break_hours

    #: L8
    required_days_float = grand_total_hours / max_hours_per_day

    #: L9
    # Round up to the nearest whole day since they need to allow for all the time.
    required_days_ceil = math.ceil(required_days_float)

    answer = required_days_ceil # FINAL ANSWER
    return answer