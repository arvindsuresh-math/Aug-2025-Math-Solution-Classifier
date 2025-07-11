def solve():
    """Index: 885.
    Returns: the total amount Bobby paid for the shoes.
    """
    # L1
    hourly_rate = 75 # charges $75 an hour
    hours_worked = 8 # for 8 hours
    labor_cost = hourly_rate * hours_worked

    # L2
    discount_rate = 0.8 # only charge 80% of the cost
    discounted_labor_cost = labor_cost * discount_rate

    # L3
    mold_cost = 250 # charges $250 to make the mold
    total_cost = discounted_labor_cost + mold_cost

    # FA
    answer = total_cost
    return answer