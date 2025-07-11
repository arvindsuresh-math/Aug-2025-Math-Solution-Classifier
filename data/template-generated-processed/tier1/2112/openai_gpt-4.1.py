def solve():
    """Index: 2112.
    Returns: the additional miles Kona drove round trip due to the bakery stop compared to without the bakery stop.
    """
    # L1
    apt_to_bakery = 9 # drives 9 miles to the bakery
    bakery_to_grandma = 24 # drives 24 miles to his grandmother’s house
    grandma_to_apt = 27 # drives 27 miles straight to his apartment
    total_with_bakery = apt_to_bakery + bakery_to_grandma + grandma_to_apt

    # L2
    total_without_bakery = grandma_to_apt + grandma_to_apt

    # L3
    additional_miles = total_with_bakery - total_without_bakery

    # FA
    answer = additional_miles
    return answer