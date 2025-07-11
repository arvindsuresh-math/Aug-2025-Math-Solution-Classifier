from fractions import Fraction

def solve():
    """Index: 1536.
    Returns: the total amount the family spent.
    """
    # L1
    ticket_cost = 5 # A movie ticket costs $5
    popcorn_percentage = Fraction(80, 100) # 80% of the cost of the ticket
    popcorn_cost = ticket_cost * popcorn_percentage

    # L2
    soda_percentage = Fraction(50, 100) # 50% of the cost of the popcorn
    soda_cost = popcorn_cost * soda_percentage

    # L3
    num_tickets = 4 # bought 4 tickets
    total_ticket_cost = ticket_cost * num_tickets

    # L4
    num_popcorn_sets = 2 # 2 sets of popcorn
    total_popcorn_cost = popcorn_cost * num_popcorn_sets

    # L5
    num_soda_cans = 4 # 4 cans of soda
    total_soda_cost = soda_cost * num_soda_cans

    # L6
    total_spent = total_ticket_cost + total_popcorn_cost + total_soda_cost

    # FA
    answer = total_spent
    return answer