def solve():
    """Index: 1030.
    Returns: the number of ounces of water left in the cooler after all cups are filled.
    """
    # L1
    gallons_in_cooler = 3 # water cooler initially contains 3 gallons
    ounces_per_gallon = 128 # WK
    initial_ounces = gallons_in_cooler * ounces_per_gallon

    # L2
    num_rows = 5 # 5 rows of meeting chairs
    chairs_per_row = 10 # 10 chairs in each row
    total_chairs = num_rows * chairs_per_row

    # L3
    ounces_per_cup = 6 # each Dixie cup holds 6 ounces of water
    total_ounces_poured = total_chairs * ounces_per_cup

    # L4
    ounces_left = initial_ounces - total_ounces_poured

    # FA
    answer = ounces_left
    return answer