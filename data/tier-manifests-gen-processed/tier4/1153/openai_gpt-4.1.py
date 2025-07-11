def solve():
    """Index: 1153.
    Returns: the total monthly cost of John's pool (cleaning and chemicals).
    """
    # L1
    days_in_month = 30 # WK (assuming a 30-day month)
    cleaning_interval_days = 3 # cleaned every 3 days
    cleanings_per_month = days_in_month / cleaning_interval_days

    # L2
    cleaning_cost = 150 # $150 each time
    tip_percent = 0.1 # 10% tip
    tip_amount = cleaning_cost * tip_percent

    # L3
    total_per_cleaning = cleaning_cost + tip_amount

    # L4
    monthly_cleaning_cost = total_per_cleaning * cleanings_per_month

    # L5
    chemical_cost_per_time = 200 # $200 of chemicals
    chemical_uses_per_month = 2 # twice a month
    monthly_chemical_cost = chemical_cost_per_time * chemical_uses_per_month

    # L6
    total_monthly_cost = monthly_cleaning_cost + monthly_chemical_cost

    # FA
    answer = total_monthly_cost
    return answer