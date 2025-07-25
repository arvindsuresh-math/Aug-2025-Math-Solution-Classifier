def solve():
    """Index: 398.
    Returns: the amount of money left after going to the pool.
    """
    # L1
    cost_per_person = 2.50 # $2.50 per person
    num_people = 10 # 10 people are going
    total_pool_cost = cost_per_person * num_people

    # L2
    initial_earnings = 30 # earned $30 total
    amount_left = initial_earnings - total_pool_cost

    # FA
    answer = amount_left
    return answer