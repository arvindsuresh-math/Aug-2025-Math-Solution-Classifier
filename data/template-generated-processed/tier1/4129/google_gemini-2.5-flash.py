def solve():
    """Index: 4129.
    Returns: the total cost for Jeremie and her friends to go to the amusement park and buy snacks.
    """
    # L1
    jeremie_count = 1 # Jeremie wants to go
    friends_count = 3 # with 3 friends
    total_people = jeremie_count + friends_count

    # L2
    ticket_cost = 18 # Tickets are $18
    snack_cost = 5 # a set of snack cost $5
    cost_per_person = ticket_cost + snack_cost

    # L3
    total_cost = cost_per_person * total_people

    # FA
    answer = total_cost
    return answer