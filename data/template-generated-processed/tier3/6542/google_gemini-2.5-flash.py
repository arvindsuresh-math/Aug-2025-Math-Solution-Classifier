def solve():
    """Index: 6542.
    Returns: the total number of paint cans Bill will need.
    """
    # L1
    gallons_per_room = 2 # Each room takes 2 gallons of paint
    num_bedrooms = 3 # The house has three bedrooms
    color_paint_gallons = gallons_per_room * num_bedrooms

    # L2
    color_can_size = 1 # Color paint comes in 1-gallon paint cans
    color_paint_cans = color_paint_gallons / color_can_size

    # L3
    other_rooms_multiplier = 2 # twice as many other rooms as bedrooms
    num_other_rooms = other_rooms_multiplier * num_bedrooms

    # L4
    white_paint_gallons = gallons_per_room * num_other_rooms

    # L5
    white_can_size = 3 # white paint comes in 3-gallon cans
    white_paint_cans = white_paint_gallons / white_can_size

    # L6
    total_cans = white_paint_cans + color_paint_cans

    # FA
    answer = total_cans
    return answer