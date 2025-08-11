def solve():
    """Index: 4979.
    Returns: the total number of hours Annie does extracurriculars before midterms.
    """
    # L1
    chess_hours_per_week = 2 # 2 hours a week on chess club
    drama_hours_per_week = 8 # 8 hours a week on drama club
    glee_hours_per_week = 3 # 3 hours a week on glee club
    total_hours_per_week = chess_hours_per_week + drama_hours_per_week + glee_hours_per_week

    # L2
    total_weeks_per_semester = 12 # 12 weeks in each semester
    midterm_divisor = 2 # dividing the total number of weeks by 2
    weeks_before_midterms = total_weeks_per_semester / midterm_divisor

    # L3
    sick_weeks = 2 # takes the first two weeks off sick
    active_weeks_before_midterms = weeks_before_midterms - sick_weeks

    # L4
    total_extracurricular_hours = total_hours_per_week * active_weeks_before_midterms

    # FA
    answer = total_extracurricular_hours
    return answer