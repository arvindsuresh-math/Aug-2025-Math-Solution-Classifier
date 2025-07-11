from fractions import Fraction

def solve():
    """Index: 2147.
    Returns: the total number of animals in the herd.
    """
    # L1
    female_hippo_fraction = Fraction(5, 7) # whose number is 5/7 of the total number of hippos
    total_initial_hippos = 35 # 35 hippos
    female_hippos = female_hippo_fraction * total_initial_hippos

    # L2
    births_per_female_hippo = 5 # give birth to 5 new baby hippos each
    new_baby_hippos = births_per_female_hippo * female_hippos

    # L3
    total_hippos = new_baby_hippos + total_initial_hippos

    # L4
    elephant_hippo_difference = 10 # ten more newborn elephants than baby hippos
    new_baby_elephants = new_baby_hippos + elephant_hippo_difference

    # L5
    total_initial_elephants = 20 # 20 elephants
    total_elephants = new_baby_elephants + total_initial_elephants

    # L6
    total_animals = total_elephants + total_hippos

    # FA
    answer = total_animals
    return answer