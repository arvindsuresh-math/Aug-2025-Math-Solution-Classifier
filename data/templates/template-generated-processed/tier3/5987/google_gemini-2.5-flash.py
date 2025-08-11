def solve():
    """Index: 5987.
    Returns: the number of shopping trips needed for the canvas bag to be the lower-carbon solution.
    """
    # L1
    bags_per_trip = 8 # eight bags per shopping trips
    oz_per_plastic_bag = 4 # each plastic bag released 4 ounces of carbon dioxide
    oz_per_trip = bags_per_trip * oz_per_plastic_bag

    # L2
    oz_per_pound = 16 # There are 16 ounces in a pound.
    pounds_per_trip = oz_per_trip / oz_per_pound

    # L3
    canvas_bag_carbon = 600 # making the canvas bag released 600 pounds of carbon dioxide
    trips_needed = canvas_bag_carbon / pounds_per_trip

    # FA
    answer = trips_needed
    return answer