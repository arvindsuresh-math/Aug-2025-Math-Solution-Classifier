from fractions import Fraction

def solve():
    """Index: 2998.
    Returns: the total number of hours Katherine's junior took to create the 30 websites.
    """
    # L1
    naomi_extra_time_fraction = Fraction(1, 4) # 1/4 times more time
    katherine_time_per_website = 20 # 20 hours to develop a website
    additional_hours_naomi = naomi_extra_time_fraction * katherine_time_per_website

    # L2
    naomi_time_per_website = katherine_time_per_website + additional_hours_naomi

    # L3
    num_websites_for_naomi = 30 # gave her junior 30 websites
    total_hours_naomi = num_websites_for_naomi * naomi_time_per_website

    # FA
    answer = total_hours_naomi
    return answer