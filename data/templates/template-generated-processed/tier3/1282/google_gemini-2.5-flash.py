def solve():
    """Index: 1282.
    Returns: the number of crayons in Judah's box.
    """
    # L1
    karen_crayons = 128 # Karen's box contained 128 crayons
    karen_beatrice_factor = 2 # twice as many crayons as were in Beatrice's box
    beatrice_crayons = karen_crayons / karen_beatrice_factor

    # L2
    beatrice_gilbert_factor = 2 # twice as many crayons as were in Gilbert's box
    gilbert_crayons = beatrice_crayons / beatrice_gilbert_factor

    # L3
    gilbert_judah_factor = 4 # four times as many crayons as were in Judah's box
    judah_crayons = gilbert_crayons / gilbert_judah_factor

    # FA
    answer = judah_crayons
    return answer