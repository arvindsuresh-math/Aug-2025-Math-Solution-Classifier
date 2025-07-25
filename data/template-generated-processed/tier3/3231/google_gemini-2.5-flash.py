from fractions import Fraction

def solve():
    """Index: 3231.
    Returns: the number of pieces of bread remaining.
    """
    # L1
    total_bread_pieces = 200 # Lucca bought 200 pieces of bread
    first_day_fraction = Fraction(1, 4) # 1/4 of the pieces of bread
    eaten_first_day = first_day_fraction * total_bread_pieces

    # L2
    remaining_after_first_day = total_bread_pieces - eaten_first_day

    # L3
    second_day_fraction = Fraction(2, 5) # 2/5 of the remaining pieces
    eaten_second_day = second_day_fraction * remaining_after_first_day

    # L4
    remaining_after_second_day = remaining_after_first_day - eaten_second_day

    # L5
    third_day_fraction = Fraction(1, 2) # half of the remaining pieces
    eaten_third_day = third_day_fraction * remaining_after_second_day

    # L6
    remaining_after_third_day = remaining_after_second_day - eaten_third_day

    # FA
    answer = remaining_after_third_day
    return answer