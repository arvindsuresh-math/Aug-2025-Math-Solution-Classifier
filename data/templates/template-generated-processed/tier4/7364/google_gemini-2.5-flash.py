import math

def solve():
    """Index: 7364.
    Returns: the number of days they should plan to study total over the next week.
    """
    # L1
    hours_per_chapter = 3 # dedicate 3 hours to each chapter of their textbook
    num_chapters = 2 # 2 chapters of their textbook
    chapter_study_hours = hours_per_chapter * num_chapters

    # L2
    hours_per_worksheet = 1.5 # 1.5 hours for each worksheet
    num_worksheets = 4 # 4 worksheets
    worksheet_study_hours = hours_per_worksheet * num_worksheets

    # Intermediate calculation for L3, L4, L7
    total_initial_study_hours = chapter_study_hours + worksheet_study_hours

    # L3
    max_hours_per_day = 4 # no more than 4 hours each day
    initial_study_days = total_initial_study_hours / max_hours_per_day

    # L4
    break_minutes_per_hour = 10 # 10-minute break every hour
    total_hourly_break_minutes = total_initial_study_hours * break_minutes_per_hour

    # L5
    num_snack_breaks = 3 # 3 10-minute snack breaks
    minutes_per_snack_break = 10 # 3 10-minute snack breaks
    total_snack_break_minutes = num_snack_breaks * minutes_per_snack_break

    # L6
    lunch_minutes_per_day = 30 # 30 minutes for lunch each day
    total_extra_minutes = total_hourly_break_minutes + total_snack_break_minutes + lunch_minutes_per_day
    minutes_per_hour = 60 # WK
    total_extra_hours = total_extra_minutes / minutes_per_hour

    # L7
    total_study_hours_with_breaks = total_initial_study_hours + total_extra_hours

    # L8
    calculated_days_needed = total_study_hours_with_breaks / max_hours_per_day

    # L9
    final_study_days = math.ceil(calculated_days_needed)

    # FA
    answer = final_study_days
    return answer