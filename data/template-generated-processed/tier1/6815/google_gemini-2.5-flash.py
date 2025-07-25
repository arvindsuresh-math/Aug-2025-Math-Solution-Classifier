def solve():
    """Index: 6815.
    Returns: the total number of animals in the zoo.
    """
    # L1
    num_tiger_enclosures = 4 # 4 tiger enclosures in a row
    multiplier_zebra_enclosures = 2 # 2 zebra enclosures
    num_zebra_enclosures = num_tiger_enclosures * multiplier_zebra_enclosures

    # L2
    multiplier_giraffe_enclosures = 3 # three times as many giraffe enclosures
    num_giraffe_enclosures = num_zebra_enclosures * multiplier_giraffe_enclosures

    # L3
    tigers_per_enclosure = 4 # The tiger enclosures hold 4 tigers
    total_tigers = num_tiger_enclosures * tigers_per_enclosure

    # L4
    zebras_per_enclosure = 10 # the zebra enclosures hold 10 zebras
    total_zebras = num_zebra_enclosures * zebras_per_enclosure

    # L5
    giraffes_per_enclosure = 2 # the giraffe enclosures hold 2 giraffes
    total_giraffes = num_giraffe_enclosures * giraffes_per_enclosure

    # L6
    total_animals = total_tigers + total_zebras + total_giraffes

    # FA
    answer = total_animals
    return answer