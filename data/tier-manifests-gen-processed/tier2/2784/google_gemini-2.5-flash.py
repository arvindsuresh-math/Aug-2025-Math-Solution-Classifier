def solve():
    """Index: 2784.
    Returns: the amount of money left from Rubble after the purchase.
    """
    # L1
    notebook_cost_per_unit = 4.00 # Each notebook cost $4.00
    num_notebooks = 2 # buy 2 notebooks
    total_notebook_cost = notebook_cost_per_unit * num_notebooks

    # L2
    pen_cost_per_unit = 1.50 # each pen cost $1.50
    num_pens = 2 # and 2 pens
    total_pen_cost = pen_cost_per_unit * num_pens

    # L3
    total_spent = total_notebook_cost + total_pen_cost

    # L4
    initial_money = 15.00 # Rubble has $15 in his pocket
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer