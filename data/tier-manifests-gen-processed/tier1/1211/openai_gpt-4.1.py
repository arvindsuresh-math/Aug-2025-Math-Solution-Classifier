def solve():
    """Index: 1211.
    Returns: the number of weeks Isabelle must work to afford the tickets.
    """
    # L1
    brother_ticket_cost = 10 # each of their tickets cost $10
    num_brothers = 2 # her two brothers
    total_brother_tickets = brother_ticket_cost * num_brothers

    # L2
    isabelle_ticket_cost = 20 # Her ticket costs $20
    total_ticket_cost = isabelle_ticket_cost + total_brother_tickets

    # L3
    brothers_saved = 5 # her brothers have saved $5 between the two of them
    isabelle_saved = 5 # Isabelle has saved $5
    total_saved = brothers_saved + isabelle_saved

    # L4
    additional_needed = total_ticket_cost - total_saved

    # L5
    weekly_pay = 3 # her job pays $3 per week
    weeks_needed = additional_needed // weekly_pay

    # FA
    answer = weeks_needed
    return answer