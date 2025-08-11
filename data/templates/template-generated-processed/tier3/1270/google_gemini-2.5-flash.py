def solve():
    """Index: 1270.
    Returns: the amount Danielle pays each month in thousands of dollars.
    """
    # L1
    purchase_price = 280 # new house for $280k
    deposit = 40 # paid a $40k deposit
    mortgage_balance = purchase_price - deposit

    # L2
    mortgage_years = 10 # spread out over 10 years
    annual_payment = mortgage_balance / mortgage_years

    # L3
    months_per_year = 12 # 12 months in a year
    monthly_payment = annual_payment / months_per_year

    # FA
    answer = monthly_payment
    return answer