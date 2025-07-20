def solve():
    """Index: 5711.
    Returns: the number of hours the bus ride needs to be for Biff to break even.
    """
    # L1
    ticket_cost = 11 # $11 on the ticket
    drinks_snacks_cost = 3 # $3 on drinks and snacks
    headphones_cost = 16 # $16 on a new pair of headphones
    total_spent = ticket_cost + drinks_snacks_cost + headphones_cost

    # L2
    gross_hourly_rate = 12 # $12/hour working online
    wifi_cost_per_hour = 2 # $2/hour to access the bus's WiFi
    net_hourly_income = gross_hourly_rate - wifi_cost_per_hour

    # L3
    hours_to_break_even = total_spent / net_hourly_income

    # FA
    answer = hours_to_break_even
    return answer