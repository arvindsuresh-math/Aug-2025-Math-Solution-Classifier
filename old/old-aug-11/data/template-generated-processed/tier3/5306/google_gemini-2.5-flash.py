def solve():
    """Index: 5306.
    Returns: the number of adults who did not wear blue.
    """
    # L1
    num_children = 45 # 45 children
    adult_fraction_denominator = 3 # one third as many adults
    total_adults = num_children / adult_fraction_denominator

    # L2
    blue_wearers_fraction_denominator = 3 # One third of the adults wore blue
    adults_wearing_blue = total_adults / blue_wearers_fraction_denominator

    # L3
    adults_not_wearing_blue = total_adults - adults_wearing_blue

    # FA
    answer = adults_not_wearing_blue
    return answer