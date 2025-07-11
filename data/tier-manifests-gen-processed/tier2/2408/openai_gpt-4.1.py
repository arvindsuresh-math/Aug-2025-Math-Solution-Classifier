def solve():
    """Index: 2408.
    Returns: Emmanuel's total charges for December including international data.
    """
    # L1
    international_data_cost_per_day = 3.50 # international data that would cost $3.50 per day
    international_days = 10 # stay in Guam in December for 10 days
    international_charge = international_data_cost_per_day * international_days

    # L2
    regular_monthly_plan = 175 # paying $175 per month for his regular plan
    total_december_charge = regular_monthly_plan + international_charge

    # FA
    answer = total_december_charge
    return answer