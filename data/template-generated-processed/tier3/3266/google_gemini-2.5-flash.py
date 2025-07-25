def solve():
    """Index: 3266.
    Returns: the number of pillows Miranda can stuff.
    """
    # L1
    goose_feathers_total = 3600 # Her goose has approximately 3600 feathers
    feathers_per_pound = 300 # A pound of goose feathers is approximately 300 feathers
    total_pounds_of_feathers = goose_feathers_total / feathers_per_pound

    # L2
    pounds_per_pillow = 2 # She needs two pounds of feathers for each pillow
    num_pillows = total_pounds_of_feathers / pounds_per_pillow

    # FA
    answer = num_pillows
    return answer