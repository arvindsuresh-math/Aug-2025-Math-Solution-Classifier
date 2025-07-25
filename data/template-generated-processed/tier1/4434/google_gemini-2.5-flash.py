def solve():
    """Index: 4434.
    Returns: the total number of theme parks in the three towns.
    """
    # L1
    jamestown_parks = 20 # Jamestown has 20 theme parks
    venice_more_than_jamestown = 25 # Venice has 25 more theme parks than Jamestown
    venice_parks = jamestown_parks + venice_more_than_jamestown

    # L2
    venice_jamestown_total = venice_parks + jamestown_parks

    # L3
    marina_del_ray_more_than_jamestown = 50 # Marina Del Ray has 50 more theme parks than Jamestown
    marina_del_ray_parks = marina_del_ray_more_than_jamestown + jamestown_parks

    # L4
    total_parks = marina_del_ray_parks + venice_jamestown_total

    # FA
    answer = total_parks
    return answer