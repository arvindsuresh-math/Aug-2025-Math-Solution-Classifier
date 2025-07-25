from fractions import Fraction

def solve():
    """Index: 4497.
    Returns: the number of cans needed to feed the reduced number of people.
    """
    # L1
    total_cans = 600 # 600 cans of stew
    initial_people = 40 # 40 people
    cans_per_person = total_cans / initial_people

    # L2
    percentage_reduction = Fraction(30, 100) # 30% fewer people
    people_reduction = percentage_reduction * initial_people

    # L3
    remaining_people = initial_people - people_reduction

    # L4
    cans_needed = cans_per_person * remaining_people

    # FA
    answer = cans_needed
    return answer