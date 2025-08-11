from fractions import Fraction

def solve():
    """Index: 6837.
    Returns: the number of crayons Annie gives to Mary.
    """
    # L1
    crayons_from_pack = 21 # pack contained 21 crayons
    crayons_in_locker = 36 # box of 36 crayons in her locker
    initial_total_crayons = crayons_from_pack + crayons_in_locker

    # L2
    bobby_divisor = 2 # half the amount she already had
    crayons_from_bobby = crayons_in_locker / bobby_divisor

    # L3
    current_total_crayons = initial_total_crayons + crayons_from_bobby

    # L4
    mary_fraction = Fraction(1, 3) # 1/3 of her total amount of crayons
    crayons_given_to_mary = current_total_crayons * mary_fraction

    # FA
    answer = crayons_given_to_mary
    return answer