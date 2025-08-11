def solve():
    """Index: 6304.
    Returns: the number of more rocks Albert collected than Joshua.
    """
    # L1
    joshua_rocks = 80 # Joshua collected 80 rocks
    jose_fewer_than_joshua = 14 # Jose collected 14 fewer rocks
    jose_rocks = joshua_rocks - jose_fewer_than_joshua

    # L2
    albert_more_than_jose = 20 # Albert has collected 20 more rocks than Jose
    albert_rocks = jose_rocks + albert_more_than_jose

    # L3
    difference_albert_joshua = albert_rocks - joshua_rocks

    # FA
    answer = difference_albert_joshua
    return answer