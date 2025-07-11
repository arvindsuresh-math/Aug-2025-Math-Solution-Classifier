def solve():
    """Index: 1638.
    Returns: the amount each person saves per month.
    """
    # L1
    years_to_save = 3 # 3 years
    months_per_year = 12 # WK
    total_months = months_per_year * years_to_save

    # L2
    downpayment = 108000 # $108000
    total_monthly_savings = downpayment / total_months

    # L3
    number_of_people = 2 # they share the monthly savings
    savings_per_person_per_month = total_monthly_savings / number_of_people

    # FA
    answer = savings_per_person_per_month
    return answer