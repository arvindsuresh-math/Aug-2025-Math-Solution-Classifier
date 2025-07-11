def solve():
    """Index: 467.
    Returns: the total distance Hadley walked in his boots in miles.
    """
    # L1
    grocery_store_miles = 2 # 2 miles to the grocery store
    pet_store_base = 2 # two miles to the pet store
    pet_store_less = 1 # 1 less than two miles
    pet_store_distance = pet_store_base - pet_store_less

    # L2
    home_base = 4 # four miles back home
    home_less = 1 # one less than four miles
    home_distance = home_base - home_less

    # L3
    total_miles_walked = grocery_store_miles + pet_store_distance + home_distance

    # FA
    answer = total_miles_walked
    return answer