from fractions import Fraction

def solve():
    """Index: 4245.
    Returns: the total number of animals hunted by all four in a day.
    """
    # L1
    rob_fraction = Fraction(1, 2) # half as many animals as Sam
    sam_animals_per_day = 6 # Sam hunts 6 animals
    rob_animals_per_day = rob_fraction * sam_animals_per_day

    # L2
    sam_and_rob_total = rob_animals_per_day + sam_animals_per_day

    # L3
    mark_fraction = Fraction(1, 3) # 1/3 of the total of what Rob and Sam hunt
    mark_animals_per_day = mark_fraction * sam_and_rob_total

    # L4
    peter_multiplier = 3 # 3 times as many animals as Mark does
    peter_animals_per_day = peter_multiplier * mark_animals_per_day

    # L5
    total_animals_hunted = sam_animals_per_day + rob_animals_per_day + mark_animals_per_day + peter_animals_per_day

    # FA
    answer = total_animals_hunted
    return answer