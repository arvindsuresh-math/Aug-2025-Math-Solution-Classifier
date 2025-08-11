def solve():
    """Index: 3993.
    Returns: the total weekly expenses to run the store.
    """
    # L1
    hours_per_day = 16 # open 16 hours a day
    days_per_week = 5 # 5 days a week
    hours_open_per_week = hours_per_day * days_per_week

    # L2
    employee_hourly_wage = 12.5 # $12.50 an hour
    employee_weekly_wage = employee_hourly_wage * hours_open_per_week

    # L3
    num_employees_per_shift = 2 # 2 employees per shift
    total_employee_wages_per_week = num_employees_per_shift * employee_weekly_wage

    # L4
    weekly_rent = 1200 # rent of $1200 a week
    utilities_rent_percentage = 0.2 # additional 20% of rent
    utilities_cost = weekly_rent * utilities_rent_percentage

    # L5
    total_weekly_expenses = weekly_rent + total_employee_wages_per_week + utilities_cost

    # FA
    answer = total_weekly_expenses
    return answer