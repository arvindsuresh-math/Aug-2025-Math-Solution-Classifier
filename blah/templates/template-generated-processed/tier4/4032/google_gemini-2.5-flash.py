from fractions import Fraction

def solve():
    """Index: 4032.
    Returns: the number of scientists from the USA.
    """
    # L1
    total_scientists = 70 # 70 scientists in total
    europe_fraction = 0.5 # Half of them are from Europe
    europe_scientists = total_scientists * europe_fraction

    # L2
    canada_fraction = Fraction(1, 5) # one-fifth are from Canada
    canada_scientists = total_scientists * canada_fraction

    # L3
    usa_scientists = total_scientists - europe_scientists - canada_scientists

    # FA
    answer = usa_scientists
    return answer