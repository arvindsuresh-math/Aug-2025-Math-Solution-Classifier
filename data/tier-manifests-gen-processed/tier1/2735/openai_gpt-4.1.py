def solve():
    """Index: 2735.
    Returns: the total amount Bob made in two weeks including regular and overtime pay.
    """
    # L1
    regular_hours_per_week = 40 # All hours over 40 in a week are considered overtime
    num_weeks = 2 # first week and second week
    total_regular_hours = regular_hours_per_week * num_weeks

    # L2
    regular_hourly_rate = 5 # $5 an hour for the regular hours
    regular_pay = total_regular_hours * regular_hourly_rate

    # L3
    week1_hours = 44 # Bob works 44  hours in the first week
    overtime_week1 = week1_hours - regular_hours_per_week

    # L4
    week2_hours = 48 # 48 hours in the second week
    overtime_week2 = week2_hours - regular_hours_per_week

    # L5
    total_overtime_hours = overtime_week2 + overtime_week1

    # L6
    overtime_hourly_rate = 6 # $6 an hour for any overtime hours
    overtime_pay = overtime_hourly_rate * total_overtime_hours

    # L7
    total_pay = regular_pay + overtime_pay

    # FA
    answer = total_pay
    return answer