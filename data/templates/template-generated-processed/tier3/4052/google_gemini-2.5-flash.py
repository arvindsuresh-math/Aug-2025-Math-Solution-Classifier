from fractions import Fraction

def solve():
    """Index: 4052.
    Returns: the combined income of Ernie and Jack.
    """
    # L1
    ernie_income_fraction = Fraction(4, 5) # 4/5 of what it used to be
    ernie_old_income = 6000 # Ernie used to make $6000
    ernie_current_income = ernie_income_fraction * ernie_old_income

    # L2
    jack_multiplier = 2 # twice what Ernie used to make
    jack_current_income = jack_multiplier * ernie_old_income

    # L3
    combined_income = jack_current_income + ernie_current_income

    # FA
    answer = combined_income
    return answer