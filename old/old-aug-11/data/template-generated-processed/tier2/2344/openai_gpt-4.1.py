def solve():
    """Index: 2344.
    Returns: Olivia's new insurance premium after one accident and three tickets.
    """
    # L1
    base_premium = 50 # insurance premium starts out at $50/month
    accident_percent_num = 10 # goes up 10% for every accident
    percent_factor = 0.01 # WK
    accident_increase = base_premium * accident_percent_num * percent_factor

    # L2
    ticket_increase_per_ticket = 5 # $5/month for every ticket
    num_tickets = 3 # 3 tickets
    ticket_increase = ticket_increase_per_ticket * num_tickets

    # L3
    new_premium = base_premium + accident_increase + ticket_increase

    # FA
    answer = new_premium
    return answer