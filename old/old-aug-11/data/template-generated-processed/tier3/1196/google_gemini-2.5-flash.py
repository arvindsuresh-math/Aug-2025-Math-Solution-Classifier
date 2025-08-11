def solve():
    """Index: 1196.
    Returns: the total age of the three brands of wine.
    """
    # L1
    carlo_rosi_age_q = 40 # the Carlo Rosi is 40 years old
    franzia_multiplier = 3 # three times as old as the Carlo Rosi
    franzia_age = franzia_multiplier * carlo_rosi_age_q

    # L2
    total_carlo_rosi_and_franzia_age = franzia_age + carlo_rosi_age_q

    # L3
    twin_valley_divisor = 4 # four times older than the Twin Valley
    twin_valley_age = carlo_rosi_age_q / twin_valley_divisor

    # L4
    total_age_three_brands = twin_valley_age + total_carlo_rosi_and_franzia_age

    # FA
    answer = total_age_three_brands
    return answer