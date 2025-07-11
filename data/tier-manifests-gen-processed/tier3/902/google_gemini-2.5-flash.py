from fractions import Fraction

def solve():
    """Index: 902.
    Returns: the number of straws each piglet ate.
    """
    # L1
    fraction_fed_to_adult_pigs = Fraction(3, 5) # 3/5 of the straws
    total_straws = 300 # Troy had 300 straws
    straws_fed_to_adult_pigs = fraction_fed_to_adult_pigs * total_straws

    # L2
    straws_for_piglets = total_straws - straws_fed_to_adult_pigs

    # L3
    num_piglets = 20 # 20 piglets
    straws_per_piglet = straws_for_piglets / num_piglets

    # FA
    answer = straws_per_piglet
    return answer