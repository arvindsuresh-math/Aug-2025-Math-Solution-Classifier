def solve():
    """Index: 4547.
    Returns: the average number of tickets sold per day.
    """
    # L1
    total_sales = 960 # tickets worth $960
    ticket_cost = 4 # One ticket costs $4
    total_tickets_sold = total_sales / ticket_cost

    # L2
    number_of_days = 3 # During three days
    average_tickets_per_day = total_tickets_sold / number_of_days

    # FA
    answer = average_tickets_per_day
    return answer