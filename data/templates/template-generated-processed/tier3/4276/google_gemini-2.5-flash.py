def solve():
    """Index: 4276.
    Returns: the number of bushes Fern needs to harvest.
    """
    # L1
    petals_per_ounce = 320 # 320 rose petals to make an ounce of perfume
    petals_per_rose = 8 # each rose produces 8 petals
    roses_per_ounce = petals_per_ounce / petals_per_rose

    # L2
    ounces_per_bottle = 12 # 12-ounce bottles of perfume
    roses_per_bottle = roses_per_ounce * ounces_per_bottle

    # L3
    num_bottles = 20 # 20 12-ounce bottles of perfume
    total_roses_needed = roses_per_bottle * num_bottles

    # L4
    roses_per_bush = 12 # 12 roses per bush
    bushes_to_harvest = total_roses_needed / roses_per_bush

    # FA
    answer = bushes_to_harvest
    return answer