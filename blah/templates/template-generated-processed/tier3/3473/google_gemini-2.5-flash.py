from fractions import Fraction

def solve():
    """Index: 3473.
    Returns: the number of eggs left for breakfast.
    """
    # L1
    num_dozens = 3 # three dozen eggs
    eggs_per_dozen = 12 # WK
    total_eggs = eggs_per_dozen * num_dozens

    # L2
    crepe_fraction = Fraction(1, 4) # 1/4 of them
    eggs_for_crepes = total_eggs * crepe_fraction

    # L3
    remaining_eggs_after_crepes = total_eggs - eggs_for_crepes

    # L4
    cupcake_fraction = Fraction(2, 3) # 2/3 of the remaining
    eggs_for_cupcakes = remaining_eggs_after_crepes * cupcake_fraction

    # L5
    eggs_left_for_breakfast = remaining_eggs_after_crepes - eggs_for_cupcakes

    # FA
    answer = eggs_left_for_breakfast
    return answer