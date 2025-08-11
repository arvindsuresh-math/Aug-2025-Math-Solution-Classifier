def solve():
    """Index: 3923.
    Returns: the number of apples Reginald sold.
    """
    # L1
    bike_cost = 80 # His bike cost $80
    repair_cost_percent = 0.25 # the repairs cost 25% of what his bike cost
    repair_cost = bike_cost * repair_cost_percent

    # L5
    # The solution implicitly solves the equation e - repair_cost = (1/5)e, which simplifies to (4/5)e = repair_cost, or e = repair_cost * (5/4).
    # Given repair_cost = 20, e = 20 * (5/4) = 25.
    # The solution directly states the result of this algebraic step.
    total_earnings = 25

    # L6
    apple_price = 1.25 # He sells each apple for $1.25
    num_apples_sold = total_earnings / apple_price

    # FA
    answer = num_apples_sold
    return answer