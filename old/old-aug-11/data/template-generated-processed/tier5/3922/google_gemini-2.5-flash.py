def solve():
    """Index: 3922.
    Returns: the number of cars to add to monthly production.
    """
    current_monthly_production = 100 # produces 100 cars per month
    target_annual_production = 1800 # reach 1800 cars per year
    months_per_year = 12 # WK

    # L3
    current_annual_production_from_current_monthly = current_monthly_production * months_per_year

    # L4
    additional_annual_production_needed = target_annual_production - current_annual_production_from_current_monthly

    # L5
    cars_to_add_monthly = additional_annual_production_needed / months_per_year

    # FA
    answer = cars_to_add_monthly
    return answer