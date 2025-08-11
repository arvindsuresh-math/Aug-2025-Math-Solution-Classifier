from fractions import Fraction

def solve():
    """Index: 6246.
    Returns: the percentage of original cookies remaining.
    """
    # L1
    total_cookies = 600 # 600 cookies in a box
    nicole_fraction = Fraction(2, 5) # 2/5 of the total number of cookies
    nicole_ate = nicole_fraction * total_cookies

    # L2
    remaining_after_nicole = total_cookies - nicole_ate

    # L3
    eduardo_fraction = Fraction(3, 5) # 3/5 of the remaining amount
    eduardo_ate = eduardo_fraction * remaining_after_nicole

    # L4
    remaining_after_eduardo = remaining_after_nicole - eduardo_ate

    # L5
    percentage_multiplier = 100 # 100%
    remaining_percentage = (remaining_after_eduardo / total_cookies) * percentage_multiplier

    # FA
    answer = remaining_percentage
    return answer