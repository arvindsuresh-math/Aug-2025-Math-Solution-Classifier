def solve():
    """Index: 4300.
    Returns: the number of days it would take Anie to finish the job.
    """
    # L1
    normal_work_hours = 10 # her work schedule requires her to be productive for 10 hours
    extra_hours = 5 # needs 5 hours extra
    total_daily_hours = normal_work_hours + extra_hours

    # L2
    project_total_hours = 1500 # project is estimated to take 1500 hours
    days_to_finish = project_total_hours / total_daily_hours

    # FA
    answer = days_to_finish
    return answer