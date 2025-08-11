from fractions import Fraction

def solve():
    """Index: 3115.
    Returns: the number of green beans.
    """
    # L1
    total_beans = 572 # 572 beans in the jar
    red_fraction = Fraction(1, 4) # One-fourth of them are red
    red_beans = total_beans * red_fraction

    # L2
    remaining_after_red = total_beans - red_beans

    # L3
    white_fraction = Fraction(1, 3) # one-third of the remaining beans are white
    white_beans = remaining_after_red * white_fraction

    # L4
    remaining_after_white = remaining_after_red - white_beans

    # L5
    green_divisor = 2 # half of the remaining are green beans
    green_beans = remaining_after_white / green_divisor

    # FA
    answer = green_beans
    return answer