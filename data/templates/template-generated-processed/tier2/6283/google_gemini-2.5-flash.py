def solve():
    """Index: 6283.
    Returns: the total cost of prom expenses.
    """
    # L1
    ticket_cost_per_person = 100 # The tickets cost $100 each
    num_people = 2 # James decides to go to prom with Susan
    total_ticket_cost = ticket_cost_per_person * num_people

    # L2
    dinner_cost = 120 # Dinner is $120
    tip_rate = 0.3 # leaves a 30% tip
    dinner_tip_amount = dinner_cost * tip_rate

    # L3
    total_dinner_cost = dinner_cost + dinner_tip_amount

    # L4
    limo_hourly_rate = 80 # cost $80 per hour
    limo_hours = 6 # for 6 hours
    total_limo_cost = limo_hourly_rate * limo_hours

    # L5
    total_cost = total_ticket_cost + total_dinner_cost + total_limo_cost

    # FA
    answer = total_cost
    return answer