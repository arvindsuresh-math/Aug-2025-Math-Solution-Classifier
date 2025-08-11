def solve():
    """Index: 1617.
    Returns: the cost in cents for Joe to make a sandwich with one slice of each protein.
    """
    # L1
    bread_cost_per_slice = 0.15 # a slice of bread costs $0.15
    bread_slices = 2 # two slices of bread per sandwich (implied by sandwich)
    bread_total_cost = bread_cost_per_slice * bread_slices

    # L2
    ham_cost_per_slice = 0.25 # a slice of ham costs $0.25
    cheese_cost_per_slice = 0.35 # a slice of cheese costs $0.35
    sandwich_total_cost = bread_total_cost + ham_cost_per_slice + cheese_cost_per_slice

    # FA
    answer = int(round(sandwich_total_cost * 100))
    return answer