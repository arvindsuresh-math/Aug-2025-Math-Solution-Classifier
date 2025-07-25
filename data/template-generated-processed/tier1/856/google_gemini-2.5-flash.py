def solve():
    """Index: 856.
    Returns: the initial amount of money Randy had in his piggy bank.
    """
    # L1
    money_per_trip = 2 # spends 2 dollars every time he goes to the store
    trips_per_month = 4 # 4 trips to the store every month
    monthly_spending = money_per_trip * trips_per_month

    # L2
    months_per_year = 12 # WK
    yearly_spending = monthly_spending * months_per_year

    # L3
    money_left_after_year = 104 # $104 dollars left in his piggy bank after a year
    initial_money = yearly_spending + money_left_after_year

    # FA
    answer = initial_money
    return answer