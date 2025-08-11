from fractions import Fraction

def solve():
    """Index: 6680.
    Returns: the number of computers John was able to fix right away.
    """
    # L1
    total_percentage = 100 # WK
    waiting_percentage = 40 # 40% of them needed to wait
    unfixable_percentage = 20 # 20% of them were unfixable
    fixed_right_away_percentage = total_percentage - waiting_percentage - unfixable_percentage

    # L2
    fixed_right_away_fraction = Fraction(fixed_right_away_percentage, 100)
    total_computers = 20 # fix 20 computers
    computers_fixed_right_away = fixed_right_away_fraction * total_computers

    # FA
    answer = computers_fixed_right_away
    return answer