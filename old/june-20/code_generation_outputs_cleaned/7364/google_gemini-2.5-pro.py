```python
import math

def solve(
    num_chapters: int = 2, # They have 2 chapters of their textbook to study
    num_worksheets: int = 4, # and 4 worksheets to memorize
    hours_per_chapter: int = 3, # dedicate 3 hours to each chapter
    hours_per_worksheet: float = 1.5, # and 1.5 hours for each worksheet
    max_study_hours_per_day: int = 4, # study no more than 4 hours each day
    break_per_hour_min: int = 10, # a 10-minute break every hour
    num_snack_breaks: int = 3, # include 3 10-minute snack breaks
    snack_break_duration_min: int = 10, # include 3 10-minute snack breaks
    lunch_duration_min: int = 30 # and 30 minutes for lunch each day
):
    """Index: 7364.
    Returns: the total number of days they should plan to study.
    """
    #: L1
    study_hours_chapters = hours_per_chapter * num_chapters
    
    #: L2
    study_hours_worksheets = hours_per_worksheet * num_worksheets
    
    #: L3
    total_study_hours = study_hours_chapters + study_hours_worksheets
    
    #: L4
    total_hourly_break_minutes = total_study_hours * break_per_hour_min
    
    #: L5
    total_snack_break_minutes = num_snack_breaks * snack_break_duration_min
    
    #: L6
    total_break_minutes = total_hourly_break_minutes + total_snack_break_minutes + lunch_duration_min
    total_break_hours = total_break_minutes / 60
    
    #: L7
    grand_total_hours = total_study_hours + total_break_hours
    
    #: L8
    days_needed_float = grand_total_hours / max_study_hours_per_day
    
    #: L9
    days_needed =