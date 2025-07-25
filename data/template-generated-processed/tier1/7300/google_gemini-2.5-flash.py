def solve():
    """Index: 7300.
    Returns: the amount of money John had left.
    """
    # L1
    days_in_april = 30 # WK
    sundays_in_april = 4 # save for the 4 Sundays in April
    days_worked = days_in_april - sundays_in_april

    # L2
    earnings_per_day = 10 # total of $10
    total_earnings = days_worked * earnings_per_day

    # L3
    cost_of_books = 50 # spent $50 on books
    given_to_kaylee = 50 # gave his sister Kaylee the same amount
    money_left = total_earnings - cost_of_books - given_to_kaylee

    # FA
    answer = money_left
    return answer