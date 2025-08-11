from fractions import Fraction

def solve():
    """Index: 5733.
    Returns: Gideon's current age.
    """
    # L1
    century_years = 100 # WK
    total_marbles = century_years # the number of marbles Gideon has

    # L2
    fraction_given_away = Fraction(3, 4) # 3/4 of the marbles
    marbles_given_away = fraction_given_away * total_marbles

    # L3
    remaining_marbles = total_marbles - marbles_given_away

    # L4
    multiplier = 2 # multiples the number of remaining marbles by 2
    age_five_years_from_now = remaining_marbles * multiplier

    # L5
    years_from_now = 5 # five years from now
    current_age = age_five_years_from_now - years_from_now

    # FA
    answer = current_age
    return answer