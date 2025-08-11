from fractions import Fraction

def solve():
    """Index: 2859.
    Returns: the amount of change Allen received.
    """
    # L1
    box_cost = 7 # cost $7 each box
    num_boxes = 5 # five boxes of pizza
    total_pizza_cost = box_cost * num_boxes

    # L2
    tip_fraction = Fraction(1, 7) # 1/7 of the total cost
    tip_amount = total_pizza_cost * tip_fraction

    # L3
    total_spent = total_pizza_cost + tip_amount

    # L4
    money_given = 100 # gave the delivery man $100
    change_received = money_given - total_spent

    # FA
    answer = change_received
    return answer