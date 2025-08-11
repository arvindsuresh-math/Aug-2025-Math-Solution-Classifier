def solve():
    """Index: 2112.
    Returns: the additional miles Kona drove with the bakery stop compared to without.
    """
    # L1
    apartment_to_bakery = 9 # drives 9 miles to the bakery
    bakery_to_grandma = 24 # drives 24 miles to his grandmother’s house
    grandma_to_apartment = 27 # drives 27 miles straight to his apartment
    total_miles_with_stop = apartment_to_bakery + bakery_to_grandma + grandma_to_apartment

    # L2
    # grandma_to_apartment is already defined from L1
    total_miles_without_stop = grandma_to_apartment + grandma_to_apartment

    # L3
    additional_miles = total_miles_with_stop - total_miles_without_stop

    # FA
    answer = additional_miles
    return answer