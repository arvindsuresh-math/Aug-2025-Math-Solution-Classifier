def solve():
    """Index: 4535.
    Returns: the total number of animals that get sick.
    """
    # L1
    chickens = 26 # 26 chickens
    sick_divisor = 2 # half of all the animals
    sick_chickens = chickens / sick_divisor

    # L2
    piglets = 40 # 40 piglets
    sick_piglets = piglets / sick_divisor

    # L3
    goats = 34 # 34 goats
    sick_goats = goats / sick_divisor

    # L4
    total_sick_animals = sick_chickens + sick_piglets + sick_goats

    # FA
    answer = total_sick_animals
    return answer