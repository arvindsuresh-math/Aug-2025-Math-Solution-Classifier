def solve():
    """Index: 1946.
    Returns: the amount of money in Randy's piggy bank after a year.
    """
    # L1
    dollars_per_trip = 2 # spends 2 dollars every time he goes to the store
    trips_per_month = 4 # makes 4 trips to the store every month
    monthly_spending = dollars_per_trip * trips_per_month

    # L2
    months_per_year = 12 # WK
    yearly_spending = monthly_spending * months_per_year

    # L3
    initial_amount = 200 # Randy has $200 in his piggy bank
    final_amount = initial_amount - yearly_spending

    # FA
    answer = final_amount
    return answer