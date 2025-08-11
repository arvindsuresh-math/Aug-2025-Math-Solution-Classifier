from fractions import Fraction

def solve():
    """Index: 3818.
    Returns: the number of balloons Anya took home.
    """
    # L1
    total_balloons = 672 # There were 672 balloons
    number_of_colors = 4 # green, blue, yellow, or red
    balloons_per_color = total_balloons / number_of_colors

    # L2
    fraction_taken = Fraction(1, 2) # half of the yellow ones
    anya_took_balloons = balloons_per_color * fraction_taken

    # FA
    answer = anya_took_balloons
    return answer