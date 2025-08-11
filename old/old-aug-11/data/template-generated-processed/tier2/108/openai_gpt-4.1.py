def solve():
    """Index: 108.
    Returns: the total amount Henry spent on pills.
    """
    # L1
    total_pills_per_day = 9 # Henry took 9 pills a day
    cheap_pills_per_day = 4 # 4 pills cost $1.50 each
    expensive_pills_per_day = total_pills_per_day - cheap_pills_per_day

    # L2
    cheap_pill_cost = 1.50 # $1.50 each
    extra_cost_per_expensive_pill = 5.50 # each cost $5.50 more
    expensive_pill_cost = cheap_pill_cost + extra_cost_per_expensive_pill

    # L3
    total_expensive_pill_cost_per_day = expensive_pill_cost * expensive_pills_per_day

    # L4
    total_cheap_pill_cost_per_day = cheap_pill_cost * cheap_pills_per_day

    # L5
    total_cost_per_day = total_expensive_pill_cost_per_day + total_cheap_pill_cost_per_day
    num_days = 14 # for 14 days
    answer = total_cost_per_day * num_days
    return answer