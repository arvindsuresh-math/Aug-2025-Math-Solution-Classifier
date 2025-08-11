def solve():
    """Index: 1030.
    Returns: the ounces of water left in the cooler.
    """
    # L1
    initial_gallons = 3 # 3 gallons of water
    ounces_per_gallon = 128 # 128 ounces in a gallon
    initial_ounces_cooler = initial_gallons * ounces_per_gallon

    # L2
    num_rows = 5 # 5 rows of meeting chairs
    chairs_per_row = 10 # 10 chairs in each row
    total_chairs = num_rows * chairs_per_row

    # L3
    cup_capacity_ounces = 6 # each Dixie cup holds 6 ounces of water
    total_ounces_poured = total_chairs * cup_capacity_ounces

    # L4
    remaining_ounces = initial_ounces_cooler - total_ounces_poured

    # FA
    answer = remaining_ounces
    return answer