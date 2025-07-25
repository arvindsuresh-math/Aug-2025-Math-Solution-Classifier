from fractions import Fraction

def solve():
    """Index: 7460.
    Returns: the total amount the school will pay for the new seats.
    """
    # L1
    seat_cost = 30 # each seat costs $30
    seats_in_group = 10 # each group of 10 seats purchased
    cost_per_group_no_discount = seat_cost * seats_in_group

    # L2
    discount_percentage = Fraction(10, 100) # 10% discount
    discount_amount_per_group = cost_per_group_no_discount * discount_percentage

    # L3
    cost_per_group_with_discount = cost_per_group_no_discount - discount_amount_per_group

    # L4
    num_rows = 5 # 5 rows of seats
    seats_per_row = 8 # Each row has 8 seats
    total_seats_to_buy = num_rows * seats_per_row

    # L5
    num_groups_of_seats = total_seats_to_buy / seats_in_group

    # L6
    total_cost = cost_per_group_with_discount * num_groups_of_seats

    # FA
    answer = total_cost
    return answer