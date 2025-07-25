from fractions import Fraction

def solve():
    """Index: 4790.
    Returns: Jacob's current age.
    """
    # L1
    rehana_current_age = 25 # Rehana is currently 25 years old
    years_in_future = 5 # In five years
    rehana_age_in_five_years = rehana_current_age + years_in_future

    # L2
    rehana_phoebe_age_multiplier = 3 # three times as old as Phoebe
    phoebe_age_in_five_years = rehana_age_in_five_years / rehana_phoebe_age_multiplier

    # L3
    phoebe_current_age = phoebe_age_in_five_years - years_in_future

    # L4
    jacob_phoebe_age_fraction = Fraction(3, 5) # Jacob, Rehana's brother, is 3/5 of Phoebe's current age
    jacob_current_age = jacob_phoebe_age_fraction * phoebe_current_age

    # FA
    answer = jacob_current_age
    return answer