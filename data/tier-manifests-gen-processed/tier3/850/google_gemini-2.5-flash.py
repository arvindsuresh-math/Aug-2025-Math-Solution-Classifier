from fractions import Fraction

def solve():
    """Index: 850.
    Returns: the total number of chips Viviana and Susana have together.
    """
    # L1
    viviana_vanilla_chips = 20 # Viviana has 20 Vanilla chips

    # L2
    susana_chocolate_chips = 25 # Susana 25 chocolate chips

    # L3
    chocolate_chip_difference = 5 # five more chocolate chips
    viviana_chocolate_chips = susana_chocolate_chips + chocolate_chip_difference

    # L4
    vanilla_chip_fraction = Fraction(3, 4) # 3/4 as many vanilla chips
    susana_vanilla_chips = vanilla_chip_fraction * viviana_vanilla_chips

    # L5
    total_chocolate_chips = viviana_chocolate_chips + susana_chocolate_chips

    # L6
    total_vanilla_chips = viviana_vanilla_chips + susana_vanilla_chips

    # L7
    total_chips = total_vanilla_chips + total_chocolate_chips

    # FA
    answer = total_chips
    return answer