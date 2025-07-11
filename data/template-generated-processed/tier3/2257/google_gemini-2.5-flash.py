def solve():
    """Index: 2257.
    Returns: the number of coconut flavored jelly beans.
    """
    # L1
    total_jelly_beans = 4000 # 4,000 jelly beans in a jar
    red_fraction_denominator = 4 # three fourths of the jelly beans are red
    red_fraction_numerator = 3 # three fourths of the jelly beans are red
    red_jelly_beans = total_jelly_beans / red_fraction_denominator * red_fraction_numerator

    # L2
    coconut_fraction_denominator = 4 # one quarter of the red jelly beans are coconut flavored
    coconut_flavored_jelly_beans = red_jelly_beans / coconut_fraction_denominator

    # FA
    answer = coconut_flavored_jelly_beans
    return answer