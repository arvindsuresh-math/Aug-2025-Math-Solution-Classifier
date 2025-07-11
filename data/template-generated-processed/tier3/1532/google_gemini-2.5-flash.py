from fractions import Fraction

def solve():
    """Index: 1532.
    Returns: the number of nails remaining in the container.
    """
    # L1
    kitchen_percentage = Fraction(30, 100) # 30% of the nails
    initial_nails = 400 # 400 nails in the container
    nails_used_kitchen = kitchen_percentage * initial_nails

    # L2
    nails_remaining_after_kitchen = initial_nails - nails_used_kitchen

    # L3
    fence_percentage = Fraction(70, 100) # 70% of the remaining nails
    nails_used_fence = fence_percentage * nails_remaining_after_kitchen

    # L4
    nails_remaining_total = nails_remaining_after_kitchen - nails_used_fence

    # FA
    answer = nails_remaining_total
    return answer