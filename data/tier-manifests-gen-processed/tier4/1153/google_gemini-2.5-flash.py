def solve():
    """Index: 1153.
    Returns: the total monthly cost of the pool.
    """
    # L1
    days_per_month = 30 # WK
    cleaning_frequency_days = 3 # every 3 days
    cleaning_times_per_month = days_per_month / cleaning_frequency_days

    # L2
    cleaning_cost_per_time = 150 # $150 each time
    tip_rate = 0.1 # 10% tip
    tip_per_cleaning = cleaning_cost_per_time * tip_rate

    # L3
    total_cost_per_cleaning = cleaning_cost_per_time + tip_per_cleaning

    # L4
    monthly_cleaning_cost = total_cost_per_cleaning * cleaning_times_per_month

    # L5
    chemical_cost_per_use = 200 # $200 of chemicals
    chemical_uses_per_month = 2 # twice a month
    monthly_chemical_cost = chemical_cost_per_use * chemical_uses_per_month

    # L6
    total_monthly_cost = monthly_cleaning_cost + monthly_chemical_cost

    # FA
    answer = total_monthly_cost
    return answer