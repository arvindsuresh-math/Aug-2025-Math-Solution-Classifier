from fractions import Fraction

def solve():
    """Index: 6842.
    Returns: the number of seats still available in the auditorium.
    """
    # L1
    total_seats = 500 # auditorium that holds 500 people
    taken_fraction_numerator = 2 # Two-fifths of the seats
    taken_fraction_denominator = 5 # Two-fifths of the seats
    seats_taken = total_seats * Fraction(taken_fraction_numerator, taken_fraction_denominator)

    # L2
    broken_fraction_numerator = 1 # 1/10 of the seats
    broken_fraction_denominator = 10 # 1/10 of the seats
    seats_broken = total_seats * Fraction(broken_fraction_numerator, broken_fraction_denominator)

    # L3
    taken_or_broken_seats = seats_taken + seats_broken

    # L4
    available_seats = total_seats - taken_or_broken_seats

    # FA
    answer = available_seats
    return answer