def solve():
    """Index: 1504.
    Returns: the total amount the theater company made from all performances.
    """
    # L1
    theater_capacity = 400 # 400 seat theater
    fill_percent = 0.8 # fill to 80% capacity
    tickets_per_day = theater_capacity * fill_percent

    # L2
    ticket_price = 30 # Each ticket cost $30
    daily_revenue = tickets_per_day * ticket_price

    # L3
    repeat_days = 2 # repeated the same performance 2 other days
    initial_day = 1 # WK: original performance day
    total_days = repeat_days + initial_day

    # L4
    total_revenue = daily_revenue * total_days

    # FA
    answer = total_revenue
    return answer