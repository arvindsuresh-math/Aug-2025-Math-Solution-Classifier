def solve():
    """Index: 115.
    Returns: the total number of jelly beans in the jar.
    """
    # L1
    coconut_flavored_jelly_beans = 750 # If 750 jelly beans are coconut flavored
    fraction_of_red_that_are_coconut_denominator = 4 # one quarter of the red jelly beans are coconut flavored
    red_jelly_beans = coconut_flavored_jelly_beans * fraction_of_red_that_are_coconut_denominator

    # L2
    fraction_of_total_that_are_red_numerator = 3 # Three fourths of the jelly beans are red
    fraction_of_total_that_are_red_denominator = 4 # Three fourths of the jelly beans are red
    total_jelly_beans = red_jelly_beans / fraction_of_total_that_are_red_numerator * fraction_of_total_that_are_red_denominator

    # FA
    answer = total_jelly_beans
    return answer