def solve(
    chapters_to_study: int = 2,  # 2 chapters of their textbook to study
    worksheets_to_memorize: int = 4,  # 4 worksheets to memorize
    hours_per_chapter: float = 3,  # 3 hours to each chapter
    hours_per_worksheet: float = 1.5,  # 1.5 hours for each worksheet
    max_study_hours_per_day: int = 4,  # plan to study no more than 4 hours each day
    break_time_per_hour: int = 10,  # 10-minute break every hour
    snack_breaks_per_day: int = 3,  # 3 10-minute snack breaks each day
    lunch_time: int = 30  # 30 minutes for lunch each day
):
    """Index: 7364.
    Returns: the number of days needed to complete their study plan."""
    #: L1
    chapter_study_time = chapters_to_study * hours_per_chapter

    #: L2
    worksheet_study_time = worksheets_to_memorize * hours_per_worksheet

    #: L3
    total_study_time = chapter_study_time + worksheet_study_time

    #: L4
    hourly_break_time = total_study_time * break_time_per_hour

    #: L5
    snack_break_time = snack_breaks_per_day * 10

    #: L6
    total_break_time = hourly_break_time + snack_break_time + lunch_time
    total_break_hours = total_break_time / 60

    #: L7
    total_time_needed = total_study_time + total_break_hours

    #: L8
    days_needed = total_time_needed / max_study_hours_per_day

    #: L9
    answer = int(days_needed + 0.99)  # Round up to the next whole day

    return answer