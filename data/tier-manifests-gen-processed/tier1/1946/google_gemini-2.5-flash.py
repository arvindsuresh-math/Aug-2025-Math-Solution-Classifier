def solve():
    """Index: 1946.
    Returns: the amount of money remaining in Randy's piggy bank after a year.
    """
    # L1
    dollars_per_trip = 2 # spends 2 dollars every time he goes to the store
    trips_per_month = 4 # makes 4 trips to the store every month
    spent_per_month = dollars_per_trip * trips_per_month

    # L2
    months_per_year = 12 # WK
    spent_per_year = spent_per_month * months_per_year

    # L3
    initial_money = 200 # Randy has $200 in his piggy bank
    remaining_money = initial_money - spent_per_year

    # FA
    answer = remaining_money
    return answer