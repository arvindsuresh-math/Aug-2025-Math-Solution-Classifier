def solve():
    """Index: 983.
    Returns: Betty's height in feet.
    """
    # L1
    dog_height_inches = 24 # 24” tall dog
    carter_height_multiplier = 2 # twice as tall
    carter_height_inches = carter_height_multiplier * dog_height_inches

    # L2
    shorter_amount_inches = 12 # 12” shorter
    betty_height_inches = carter_height_inches - shorter_amount_inches

    # L3
    inches_per_foot = 12 # 12" is the same as 1 foot
    betty_height_feet = betty_height_inches / inches_per_foot

    # FA
    answer = betty_height_feet
    return answer