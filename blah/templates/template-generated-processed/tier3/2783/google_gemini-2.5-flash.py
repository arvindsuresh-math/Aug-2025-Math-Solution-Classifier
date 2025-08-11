def solve():
    """Index: 2783.
    Returns: the cost of each chair.
    """
    # L1
    cost_per_set_plates = 20 # $20 for each set
    num_sets_plates = 2 # two sets of plates
    total_cost_plates = cost_per_set_plates * num_sets_plates

    # L2
    cost_table = 50 # a table that costs $50
    total_cost_table_and_plates = cost_table + total_cost_plates

    # L3
    cash_given = 130 # After giving the cashier $130
    change_received = 4 # got a $4 change
    total_paid = cash_given - change_received

    # L4
    total_cost_chairs = total_paid - total_cost_table_and_plates

    # L5
    num_chairs = 3 # three chairs
    cost_per_chair = total_cost_chairs / num_chairs

    # FA
    answer = cost_per_chair
    return answer