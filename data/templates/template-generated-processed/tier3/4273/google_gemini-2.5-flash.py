from fractions import Fraction

def solve():
    """Index: 4273.
    Returns: the total number of animals Brinley counted at the zoo.
    """
    # L1
    bee_eaters_multiplier = 10 # ten times more bee-eaters
    leopards = 20 # 20 leopards
    bee_eaters = bee_eaters_multiplier * leopards

    # L2
    cheetahs_fraction = Fraction(1, 2) # half as many cheetahs
    snakes = 100 # 100 snakes
    cheetahs = cheetahs_fraction * snakes

    # L3
    arctic_foxes = 80 # 80 arctic foxes
    total_foxes_leopards = arctic_foxes + leopards

    # L4
    alligators_multiplier = 2 # twice as many alligators
    alligators = alligators_multiplier * total_foxes_leopards

    # L5
    bee_eaters_L5_value = 220 # 220 bee-eaters
    total_animals = alligators + bee_eaters_L5_value + snakes + arctic_foxes + leopards + cheetahs

    # FA
    answer = total_animals
    return answer