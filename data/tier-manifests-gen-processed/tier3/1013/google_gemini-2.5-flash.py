def solve():
    """Index: 1013.
    Returns: the number of striped jerseys Justin bought.
    """
    # L1
    long_sleeved_quantity = 4 # four long-sleeved ones
    long_sleeved_cost_per_jersey = 15 # cost $15 each
    long_sleeved_total_cost = long_sleeved_cost_per_jersey * long_sleeved_quantity

    # L2
    total_spent = 80 # spent a total of $80
    striped_total_cost = total_spent - long_sleeved_total_cost

    # L3
    striped_cost_per_jersey = 10 # cost $10 each
    striped_quantity = striped_total_cost / striped_cost_per_jersey

    # FA
    answer = striped_quantity
    return answer