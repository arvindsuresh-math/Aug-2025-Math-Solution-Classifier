def solve(
    num_chapters: int = 2, # 2 chapters of their textbook to study
    num_worksheets: int = 4, # 4 worksheets to memorize
    hours_per_chapter: float = 3, # dedicate 3 hours to each chapter
    hours_per_worksheet: float = 1.5, # 1.5 hours for each worksheet
    max_study_hours_per_day: int = 4, # study no more than 4 hours each day
    break_minutes_per_hour: int = 10, # 10-minute break every hour
    snack_breaks_per_day: int = 3, # 3 10-minute snack breaks each day
    snack_break_minutes: int = 10, # 10-minute snack breaks
    lunch_minutes_per_day: int = 30 # 30 minutes for lunch each day
):
    """Index: 7364.
    Returns: the total number of days they should plan to study over the next week.
    """
    #: L1
    chapter_study_hours = hours_per_chapter * num_chapters

    #: L2
    worksheet_study_hours = hours_per_worksheet * num_worksheets

    #: L3
    total_study_hours = chapter_study_hours + worksheet_study_hours

    #: L4
    total_break_minutes = total_study_hours * break_minutes_per_hour

    #: L5
    total_snack_minutes = snack_breaks_per_day * snack_break_minutes

    #: L6
    total_extra_minutes = total_break_minutes + total_snack_minutes + lunch_minutes_per_day
    total_extra_hours = total_extra_minutes / 60

    #: L7
    total_hours_with_breaks = total_study_hours + total_extra_hours

    #: L8
    days_needed = total_hours_with_breaks / max_study_hours_per_day

    #: L9
    answer = int(-(-days_needed // 1)) # FINAL ANSWER (round up to next whole day)
    return answer