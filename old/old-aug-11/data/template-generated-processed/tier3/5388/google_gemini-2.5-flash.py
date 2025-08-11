from fractions import Fraction

def solve():
    """Index: 5388.
    Returns: the number of large posters.
    """
    # L1
    total_posters = 50 # 50 posters
    small_fraction = Fraction(2, 5) # Two-fifths of them are small posters
    small_posters = total_posters * small_fraction

    # L2
    medium_divisor = 2 # half of them are medium posters
    medium_posters = total_posters / medium_divisor

    # L3
    not_large_posters = small_posters + medium_posters

    # L4
    large_posters = total_posters - not_large_posters

    # FA
    answer = large_posters
    return answer