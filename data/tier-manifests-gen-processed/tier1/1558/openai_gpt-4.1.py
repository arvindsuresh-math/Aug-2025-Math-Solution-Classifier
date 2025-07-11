def solve():
    """Index: 1558.
    Returns: how much more Janet would make per month as a freelancer than at her current job.
    """
    # L1
    freelancer_hourly = 40 # would get paid $40/hour as a freelancer
    current_hourly = 30 # get paid $30/hour at her current job
    hourly_difference = freelancer_hourly - current_hourly

    # L2
    hours_per_week = 40 # works 40 hours a week at both jobs
    weekly_difference = hourly_difference * hours_per_week

    # L3
    weeks_per_month = 4 # four weeks in a month
    monthly_difference = weekly_difference * weeks_per_month

    # L4
    fica_per_week = 25 # pay an extra $25 a week in FICA taxes
    monthly_fica = fica_per_week * weeks_per_month

    # L5
    healthcare_per_month = 400 # $400/month in healthcare premiums
    net_increase = monthly_difference - healthcare_per_month - monthly_fica

    # FA
    answer = net_increase
    return answer