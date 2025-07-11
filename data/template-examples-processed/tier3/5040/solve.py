from fractions import Fraction

def solve():
    """Index: 5040.
    Returns: the number of ducks remaining after three nights.
    """
    # L1
    initial_ducks = 320 # 320 ducks in a pond
    first_night_eaten_fraction = Fraction(1, 4) # 1/4 of them get eaten
    first_night_eaten = initial_ducks * first_night_eaten_fraction

    # L2
    ducks_after_night1 = initial_ducks - first_night_eaten

    # L3
    second_night_flew_fraction = Fraction(1, 6) # 1/6 of the remaining ducks fly away
    second_night_flew = ducks_after_night1 * second_night_flew_fraction

    # L4
    ducks_after_night2 = ducks_after_night1 - second_night_flew

    # L5
    third_night_stolen_percent = 0.30 # 30 percent are stolen
    third_night_stolen = ducks_after_night2 * third_night_stolen_percent

    # L6
    ducks_after_night3 = ducks_after_night2 - third_night_stolen

    # FA
    answer = ducks_after_night3
    return answer