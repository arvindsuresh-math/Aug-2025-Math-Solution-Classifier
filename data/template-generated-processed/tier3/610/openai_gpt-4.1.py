from fractions import Fraction

def solve():
    """Index: 610.
    Returns: the number of pies that are not eaten with forks.
    """
    # L1
    pies_with_fork_percentage = Fraction(68, 100) # 68% of all pies are eaten with forks
    total_pies = 2000 # there are 2000 pies of all kinds
    pies_eaten_with_forks = pies_with_fork_percentage * total_pies

    # L2
    pies_not_eaten_with_forks = total_pies - pies_eaten_with_forks

    # FA
    answer = pies_not_eaten_with_forks
    return answer