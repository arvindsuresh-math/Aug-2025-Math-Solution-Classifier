from fractions import Fraction

def solve():
    """Index: 1271.
    Returns: the amount of money Dorothy will have left after the trip.
    """
    # L1
    regular_ticket_cost = 10 # The regular ticket cost is $10
    discount_percentage = Fraction(30, 100) # discount of 30%
    discount_per_ticket = regular_ticket_cost * discount_percentage

    # L2
    num_discounted_tickets = 2 # Dorothy is 15 years old and her younger brother
    total_discount = num_discounted_tickets * discount_per_ticket

    # L3
    total_family_members = 5 # Her family consists of her, her younger brother, her parents, and her grandfather
    total_cost_no_discount = total_family_members * regular_ticket_cost

    # L4
    final_ticket_cost = total_cost_no_discount - total_discount

    # L5
    dorothy_initial_money = 70 # she currently has $70
    money_left = dorothy_initial_money - final_ticket_cost

    # FA
    answer = money_left
    return answer