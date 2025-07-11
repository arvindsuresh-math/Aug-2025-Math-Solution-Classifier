def solve():
    """Index: 2774.
    Returns: the average number of tickets Officer Hopps has to give out each day for the rest of the month.
    """
    # L1
    days_first_period = 15 # The first 15 days
    avg_tickets_first_period = 8 # averages 8 tickets a day
    tickets_given_first_period = days_first_period * avg_tickets_first_period

    # L2
    total_days_in_may = 31 # WK
    remaining_days = total_days_in_may - days_first_period

    # L3
    total_tickets_goal = 200 # give out 200 tickets in May
    tickets_remaining_to_give = total_tickets_goal - tickets_given_first_period

    # L4
    avg_tickets_per_day_remaining = tickets_remaining_to_give / remaining_days

    # FA
    answer = avg_tickets_per_day_remaining
    return answer