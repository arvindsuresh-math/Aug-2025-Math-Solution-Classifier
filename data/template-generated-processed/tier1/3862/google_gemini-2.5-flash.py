def solve():
    """Index: 3862.
    Returns: the total money Doctor Lyndsay receives in a typical 8-hour day.
    """
    # L1
    adult_patients_per_hour = 4 # 4 adult patients
    cost_adult_visit = 50 # cost for an adult's office visit is $50
    revenue_adult_per_hour = adult_patients_per_hour * cost_adult_visit

    # L2
    child_patients_per_hour = 3 # 3 child patients
    cost_child_visit = 25 # cost for a child's office visit is $25
    revenue_child_per_hour = child_patients_per_hour * cost_child_visit

    # L3
    total_revenue_per_hour = revenue_adult_per_hour + revenue_child_per_hour

    # L4
    work_hours_per_day = 8 # typical 8-hour day
    total_revenue_per_day = work_hours_per_day * total_revenue_per_hour

    # FA
    answer = total_revenue_per_day
    return answer