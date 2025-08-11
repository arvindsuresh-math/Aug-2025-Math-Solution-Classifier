def solve():
    """Index: 3117.
    Returns: the total amount Mark paid.
    """
    # L1
    hourly_rate = 15 # $15 an hour
    hours_hired = 3 # for 3 hours
    base_cost = hourly_rate * hours_hired

    # L2
    tip_percentage = 0.2 # tips the singer 20%
    tip_amount = base_cost * tip_percentage

    # L3
    total_paid = base_cost + tip_amount

    # FA
    answer = total_paid
    return answer