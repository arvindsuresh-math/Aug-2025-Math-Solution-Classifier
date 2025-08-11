def solve():
    """Index: 5343.
    Returns: the total phone bill for the entire next year.
    """
    # L1
    usual_monthly_bill = 50 # $50 a month
    increase_percentage_numerator = 110 # increases by 10%
    percentage_denominator = 100 # 110/100
    new_monthly_bill = usual_monthly_bill * increase_percentage_numerator / percentage_denominator

    # L2
    months_per_year = 12 # entire next year
    annual_bill = new_monthly_bill * months_per_year

    # FA
    answer = annual_bill
    return answer