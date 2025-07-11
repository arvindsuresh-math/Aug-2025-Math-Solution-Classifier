from fractions import Fraction

def solve():
    """Index: 40.
    Returns: the total amount Mr. Benson paid.
    """
    # L1
    total_tickets_bought = 12 # bought 12 tickets
    threshold_for_discount = 10 # exceeds 10
    discounted_tickets_count = total_tickets_bought - threshold_for_discount

    # L2
    original_ticket_cost = 40 # A concert ticket costs $40
    discount_percentage = Fraction(5, 100) # 5% discount
    discount_per_ticket = original_ticket_cost * discount_percentage

    # L3
    discounted_ticket_price = original_ticket_cost - discount_per_ticket

    # L4
    cost_of_discounted_tickets = discounted_ticket_price * discounted_tickets_count

    # L5
    non_discounted_tickets_count = 10 # the other ten tickets
    cost_of_non_discounted_tickets = original_ticket_cost * non_discounted_tickets_count

    # L6
    total_paid = cost_of_non_discounted_tickets + cost_of_discounted_tickets

    # FA
    answer = total_paid
    return answer