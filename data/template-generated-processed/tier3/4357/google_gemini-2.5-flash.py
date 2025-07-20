from fractions import Fraction

def solve():
    """Index: 4357.
    Returns: the number of seats usually taken in the cafeteria.
    """
    # L1
    num_tables = 15 # 15 tables
    seats_per_table = 10 # Each table can seat 10 people
    total_capacity = num_tables * seats_per_table

    # L2
    unseated_fraction = Fraction(1, 10) # 1/10 of the seats
    unseated_seats = total_capacity * unseated_fraction

    # L3
    taken_seats = total_capacity - unseated_seats

    # FA
    answer = taken_seats
    return answer