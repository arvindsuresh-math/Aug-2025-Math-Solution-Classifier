from fractions import Fraction

def solve():
    """Index: 6285.
    Returns: the number of goldfish Maggie still needs to catch.
    """
    # L1
    total_goldfish_in_aquarium = 100 # 100 goldfish in the aquarium
    allowed_fraction = Fraction(1, 2) # half of them
    allowed_goldfish = allowed_fraction * total_goldfish_in_aquarium

    # L2
    caught_fraction = Fraction(3, 5) # caught 3/5 of the total number of goldfish she was allowed to take home
    caught_goldfish = caught_fraction * allowed_goldfish

    # L3
    remaining_to_catch = allowed_goldfish - caught_goldfish

    # FA
    answer = remaining_to_catch
    return answer