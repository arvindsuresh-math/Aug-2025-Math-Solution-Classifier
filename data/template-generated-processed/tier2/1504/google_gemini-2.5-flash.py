def solve():
    """Index: 1504.
    Returns: the total amount of money the theater company made.
    """
    # L1
    theater_capacity = 400 # 400 seat theater
    capacity_fill_percent = 0.8 # fill to 80% capacity
    tickets_sold_per_day = theater_capacity * capacity_fill_percent

    # L2
    ticket_cost = 30 # Each ticket cost $30
    revenue_per_day = tickets_sold_per_day * ticket_cost

    # L3
    other_performance_days = 2 # repeated the same performance 2 other days
    initial_performance_day = 1 # WK
    total_performance_days = other_performance_days + initial_performance_day

    # L4
    total_revenue = revenue_per_day * total_performance_days

    # FA
    answer = total_revenue
    return answer