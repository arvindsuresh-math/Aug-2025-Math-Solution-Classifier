from fractions import Fraction

def solve():
    """Index: 610.
    Returns: the number of pies not eaten with forks.
    """
    # L1
    total_pies = 2000 # 2000 pies of all kinds
    eaten_with_forks_percentage = Fraction(68, 100) # 68% of all pies are eaten with forks
    pies_eaten_with_forks = eaten_with_forks_percentage * total_pies

    # L2
    pies_not_eaten_with_forks = total_pies - pies_eaten_with_forks

    # FA
    answer = pies_not_eaten_with_forks
    return answer