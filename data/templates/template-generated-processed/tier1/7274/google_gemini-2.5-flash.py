def solve():
    """Index: 7274.
    Returns: the odds a candidate knows Excel and is willing to work nights.
    """
    # L1
    total_percentage = 100 # WK
    willing_day_shifts_percent = 70 # 70% of the candidates are only willing to work day shifts
    willing_night_shifts_percent = total_percentage - willing_day_shifts_percent

    # L2
    excel_experience_percent = 20 # 20% of the job candidates at a temp agency have experience with Excel
    both_qualifications_percent = (willing_night_shifts_percent * excel_experience_percent) / 100

    # FA
    answer = both_qualifications_percent
    return answer