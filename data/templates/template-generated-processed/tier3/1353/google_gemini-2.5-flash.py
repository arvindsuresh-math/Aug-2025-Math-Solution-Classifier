def solve():
    """Index: 1353.
    Returns: the height of the camel in feet.
    """
    # L1
    hare_height_inches = 14 # a hare is 14 inches tall
    taller_factor = 24 # a camel is 24 times taller than the hare
    camel_height_inches = hare_height_inches * taller_factor

    # L2
    inches_per_foot = 12 # WK
    camel_height_feet = camel_height_inches / inches_per_foot

    # FA
    answer = camel_height_feet
    return answer