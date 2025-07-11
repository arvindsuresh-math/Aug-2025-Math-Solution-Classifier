def solve():
    """Index: 115.
    Returns: the total number of jelly beans in the jar.
    """
    # L1
    coconut_flavored = 750 # 750 jelly beans are coconut flavored
    red_fraction_denominator = 4 # one quarter of the red jelly beans
    red_jelly_beans = coconut_flavored * red_fraction_denominator

    # L2
    red_fraction_numerator = 3 # Three fourths of the jelly beans are red
    total_jelly_beans = red_jelly_beans / red_fraction_numerator * red_fraction_denominator

    # FA
    answer = total_jelly_beans
    return answer