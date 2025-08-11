from fractions import Fraction

def solve():
    """Index: 4085.
    Returns: the number of ants in the third anthill.
    """
    # L1
    percentage_fewer = Fraction(20, 100) # 20% fewer ants
    first_anthill_ants = 100 # In the first anthill, there are 100 ants
    ants_less_second_anthill = percentage_fewer * first_anthill_ants

    # L2
    second_anthill_ants = first_anthill_ants - ants_less_second_anthill

    # L3
    ants_less_third_anthill = percentage_fewer * second_anthill_ants

    # L4
    third_anthill_ants = second_anthill_ants - ants_less_third_anthill

    # FA
    answer = third_anthill_ants
    return answer