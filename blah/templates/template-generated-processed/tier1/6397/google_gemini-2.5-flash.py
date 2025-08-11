def solve():
    """Index: 6397.
    Returns: the amount of money Casey would save per week by hiring the cheaper employee.
    """
    # L1
    employee1_hourly_rate = 20 # $20 an hour
    hours_per_week = 40 # 40 hours per week
    employee1_weekly_cost = employee1_hourly_rate * hours_per_week

    # L2
    employee2_hourly_rate_before_subsidy = 22 # $22 an hour
    government_subsidy_per_hour = 6 # $6/hour subsidy
    employee2_hourly_cost_after_subsidy = employee2_hourly_rate_before_subsidy - government_subsidy_per_hour

    # L3
    employee2_weekly_cost = employee2_hourly_cost_after_subsidy * hours_per_week

    # L4
    weekly_savings = employee1_weekly_cost - employee2_weekly_cost

    # FA
    answer = weekly_savings
    return answer