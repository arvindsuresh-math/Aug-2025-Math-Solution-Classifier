def solve():
    """Index: 895.
    Returns: the number of gallons of paint Henrietta needs.
    """
    # L1
    num_bedrooms = 3 # three bedrooms
    sq_ft_per_bedroom = 400 # each bedroom take up 400 square feet
    total_bedroom_sq_ft = num_bedrooms * sq_ft_per_bedroom

    # L2
    living_room_sq_ft = 600 # The walls in the living room take up 600 square feet
    total_house_sq_ft = total_bedroom_sq_ft + living_room_sq_ft

    # L3
    sq_ft_per_gallon = 600 # one gallon of paint can cover 600 square feet
    gallons_needed = total_house_sq_ft / sq_ft_per_gallon

    # FA
    answer = gallons_needed
    return answer