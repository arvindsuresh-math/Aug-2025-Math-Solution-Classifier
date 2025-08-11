def solve():
    """Index: 3111.
    Returns: the amount of money John saves a year.
    """
    # L1
    old_apartment_sq_ft = 750 # 750 square foot apartment
    old_rent_per_sq_ft = 2 # $2 per square foot
    old_monthly_rent = old_apartment_sq_ft * old_rent_per_sq_ft

    # L2
    new_apartment_cost_per_month = 2800 # $2800 per month
    number_of_roommates = 2 # splits evenly with the roommate
    new_monthly_rent_share = new_apartment_cost_per_month / number_of_roommates

    # L3
    monthly_savings = old_monthly_rent - new_monthly_rent_share

    # L4
    months_per_year = 12 # WK
    annual_savings = monthly_savings * months_per_year

    # FA
    answer = annual_savings
    return answer