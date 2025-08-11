def solve():
    """Index: 4062.
    Returns: the percentage of Jenna's monthly salary spent on the outing.
    """
    # L1
    num_drink_tickets = 5 # five drink tickets
    cost_per_drink_ticket = 7 # $7 each
    total_drink_cost = num_drink_tickets * cost_per_drink_ticket

    # L2
    concert_ticket_cost = 181 # concert ticket that costs $181
    total_outing_cost = total_drink_cost + concert_ticket_cost

    # L3
    hourly_rate = 18 # earns $18 an hour
    hours_per_week = 30 # works 30 hours a week
    weekly_earnings = hourly_rate * hours_per_week

    # L4
    weeks_per_month = 4 # WK
    monthly_salary = weekly_earnings * weeks_per_month

    # L5
    percentage_multiplier = 100 # WK
    percentage_of_salary = (total_outing_cost / monthly_salary) * percentage_multiplier

    # FA
    answer = percentage_of_salary
    return answer