from fractions import Fraction

def solve():
    """Index: 5460.
    Returns: the number of ounces left in the cup afterward.
    """
    # L1
    total_cup_ounces = 12 # 12-ounce cup of coffee
    on_way_to_work_fraction = Fraction(1, 4) # one-quarter of the cup
    drank_on_way_to_work = on_way_to_work_fraction * total_cup_ounces

    # L2
    at_office_fraction = Fraction(1, 2) # another half of the cup
    drank_at_office = at_office_fraction * total_cup_ounces

    # L3
    drank_cold_coffee = 1 # only drinks 1 ounce of the remaining amount
    total_drank = drank_on_way_to_work + drank_at_office + drank_cold_coffee

    # L4
    ounces_left = total_cup_ounces - total_drank

    # FA
    answer = ounces_left
    return answer