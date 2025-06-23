import math

def solve(
    num_chapters: int = 2, # They have 2 chapters
    num_worksheets: int = 4, # and 4 worksheets
    hours_per_chapter: int = 3, # dedicate 3 hours to each chapter
    hours_per_worksheet: float = 1.5, # and 1.5 hours for each worksheet
    max_hours_per_day: int = 4, # study no more than 4 hours each day
    break_minutes_per_hour: int = 10, # take a 10-minute break every hour
    num_snack_breaks: int = 3, # include 3 10-minute snack breaks each day
    snack_break_minutes: int = 10, # include 3 10-minute snack breaks each day
    lunch_minutes: int = 30 # and 30 minutes for lunch each day
):
    """Index: 7364.
    Returns: the total number of days they should plan to study.
    """
    #: L1
    chapter_study_time = hours_per_chapter * num_chapters

    #: L2
    worksheet_study_time = hours_per_worksheet * num_worksheets

    # Calculate total core study time (without breaks)
    initial_study_hours = chapter_study_time + worksheet_study_time

    #: L3
    # This step calculates initial days based on study time only, not used in final day calculation
    # initial_days = initial_study_hours / max_hours_per_day

    #: L4
    # Calculate total break time from hourly breaks over the total study hours
    hourly_break_minutes_total = initial_study_hours * break_minutes_per_hour

    #: L5
    # Calculate total time for snack breaks
    snack_break_minutes_total = num_snack_breaks * snack_break_minutes

    #: L6
    # Calculate total extra time (breaks + lunch) in minutes
    total_extra_minutes = hourly_break_minutes_total + snack_break_minutes_total + lunch_minutes
    # Convert total extra time to hours
    total_extra_hours = total_extra_minutes / 60

    #: L7
    # Calculate total time needed including study and all breaks
    total_time_needed_with_breaks = initial_study_hours + total_extra_hours

    #: L8
    # Calculate the number of days needed based on the maximum hours per day
    days_needed_float = total_time_needed_with_breaks / max_hours_per_day

    #: L9
    # Since they can't study for a fraction of a day to complete the task, round up to the nearest whole day
    days_needed_ceil = math.ceil(days_needed_float)

    answer = days_needed_ceil # FINAL ANSWER
    return answer