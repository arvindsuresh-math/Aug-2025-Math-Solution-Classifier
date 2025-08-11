def solve():
    """Index: 2799.
    Returns: the number of hours Jake had to work.
    """
    # L1
    total_debt = 100 # owed someone $100
    paid_amount = 40 # paid them $40
    remaining_debt = total_debt - paid_amount

    # L2
    hourly_rate = 15 # worked for $15 an hour
    hours_to_work = remaining_debt / hourly_rate

    # FA
    answer = hours_to_work
    return answer