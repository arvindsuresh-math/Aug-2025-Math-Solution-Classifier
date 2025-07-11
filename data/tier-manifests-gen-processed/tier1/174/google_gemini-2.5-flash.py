def solve():
    """Index: 174.
    Returns: the total amount Glenn spends on movie tickets.
    """
    # L1
    monday_ticket_cost = 5 # Movie tickets cost $5 each on a Monday
    wednesday_multiplier = 2 # twice as much on a Wednesday
    wednesday_cost = monday_ticket_cost * wednesday_multiplier

    # L2
    saturday_multiplier = 5 # five times as much as Monday on a Saturday
    saturday_cost = monday_ticket_cost * saturday_multiplier

    # L3
    total_spent = wednesday_cost + saturday_cost

    # FA
    answer = total_spent
    return answer