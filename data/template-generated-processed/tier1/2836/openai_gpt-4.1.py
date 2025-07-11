def solve():
    """Index: 2836.
    Returns: the total number of fish fillets Luke has after 30 days.
    """
    # L1
    fish_per_day = 2 # catches 2 fish every day
    num_days = 30 # for 30 days
    total_fish = fish_per_day * num_days

    # L2
    fillets_per_fish = 2 # each fish gives him 2 fillets
    total_fillets = fillets_per_fish * total_fish

    # FA
    answer = total_fillets
    return answer