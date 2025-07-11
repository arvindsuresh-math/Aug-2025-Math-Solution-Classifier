def solve():
    """Index: 1387.
    Returns: the number of pieces of gum each person will get.
    """
    # L1
    johns_gum = 54 # John has 54 pieces of gum
    coles_gum = 45 # Cole has 45 pieces of gum
    aubreys_gum = 0 # Aubrey has no pieces of gum
    total_gum_pieces = johns_gum + coles_gum + aubreys_gum

    # L2
    number_of_people = 3 # between the 3 of them
    gum_per_person = total_gum_pieces / number_of_people

    # FA
    answer = gum_per_person
    return answer