def solve():
    """Index: 398.
    Returns: the amount of money the girl scouts have left after paying for the pool.
    """
    # L1
    cost_per_person = 2.5 # $2.50 per person to go
    num_people = 10 # 10 people are going
    total_pool_cost = cost_per_person * num_people

    # L2
    total_earned = 30 # earned $30 total from selling cookies
    amount_left = total_earned - total_pool_cost

    # FA
    answer = amount_left
    return answer