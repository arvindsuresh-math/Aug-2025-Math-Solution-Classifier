from fractions import Fraction

def solve():
    """Index: 83.
    Returns: the number of hats each person gets after sharing.
    """
    # L1
    paityn_red_hats = 20 # 20 red hats
    paityn_blue_hats = 24 # 24 blue hats
    paityn_total_hats = paityn_red_hats + paityn_blue_hats

    # L2
    zola_red_hats_fraction = Fraction(4, 5) # 4/5 times as many red hats
    zola_red_hats = zola_red_hats_fraction * paityn_red_hats

    # L3
    zola_blue_hats_multiplier = 2 # twice the number of blue hats
    zola_blue_hats = zola_blue_hats_multiplier * paityn_blue_hats

    # L4
    zola_total_hats = zola_blue_hats + zola_red_hats

    # L5
    combined_hats = zola_total_hats + paityn_total_hats

    # L6
    number_of_people = 2 # share them equally between themselves
    hats_per_person = combined_hats / number_of_people

    # FA
    answer = hats_per_person
    return answer