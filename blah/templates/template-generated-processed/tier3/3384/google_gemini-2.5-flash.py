def solve():
    """Index: 3384.
    Returns: the number of bottles Barry needs to buy.
    """
    # L1
    capsules_per_bottle = 60 # bottles containing 60 capsules
    serving_size_capsules = 2 # daily serving size of 2 capsules
    servings_per_bottle = capsules_per_bottle / serving_size_capsules

    # L2
    total_days = 180 # for 180 days
    bottles_needed = total_days / servings_per_bottle

    # FA
    answer = bottles_needed
    return answer