from fractions import Fraction

def solve():
    """Index: 1215.
    Returns: the number of 1L milk cartons Brian needs to buy.
    """
    # L1
    brian_count = 1 # Brian
    wife_count = 1 # his wife
    kids_count = 2 # his two kids
    parents_count = 2 # his parents
    in_laws_count = 2 # his wife's parents
    total_people = brian_count + wife_count + kids_count + parents_count + in_laws_count

    # L2
    servings_per_person = 2 # each person is expected to eat 2 servings
    total_servings = total_people * servings_per_person

    # L3
    milk_per_serving = Fraction(1, 2) # 1/2 a cup of milk per serving
    total_cups_milk = total_servings * milk_per_serving

    # L4
    ml_per_cup = 250 # One US cup equals 250ml
    total_ml_milk = total_cups_milk * ml_per_cup

    # L5
    ml_per_liter = 1000 # WK
    liter_carton_size = 1 # 1L cartons
    cartons_needed = total_ml_milk / ml_per_liter

    # FA
    answer = cartons_needed
    return answer