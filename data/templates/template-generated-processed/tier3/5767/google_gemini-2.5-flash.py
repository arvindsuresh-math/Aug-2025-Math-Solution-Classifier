from fractions import Fraction

def solve():
    """Index: 5767.
    Returns: the number of bananas Walter gets after sharing.
    """
    # L1
    fewer_fraction = Fraction(1, 4) # 1/4 times fewer bananas
    jefferson_bananas = 56 # Jefferson has 56 bananas
    fewer_bananas_walter_has = fewer_fraction * jefferson_bananas

    # L2
    walter_bananas = jefferson_bananas - fewer_bananas_walter_has

    # L3
    total_combined_bananas = walter_bananas + jefferson_bananas

    # L4
    number_of_people_sharing = 2 # share them equally between themselves
    walter_gets_after_sharing = total_combined_bananas / number_of_people_sharing

    # FA
    answer = walter_gets_after_sharing
    return answer