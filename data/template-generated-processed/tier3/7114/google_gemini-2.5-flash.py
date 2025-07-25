def solve():
    """Index: 7114.
    Returns: the cost of each barbell.
    """
    # L1
    amount_given = 850 # gives $850
    change_received = 40 # gets $40 in change
    total_price_barbells = amount_given - change_received

    # L2
    num_barbells = 3 # buys 3 barbells
    cost_per_barbell = total_price_barbells / num_barbells

    # FA
    answer = cost_per_barbell
    return answer