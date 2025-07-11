def solve():
    """Index: 1010.
    Returns: the time it will take Erin to serve all the soup, rounded to the nearest minute.
    """
    # L1
    ounces_per_bowl = 10 # Each bowl of soup has 10 ounces
    bowls_per_minute = 5 # Erin can serve 5 bowls per minute
    ounces_per_minute = ounces_per_bowl * bowls_per_minute

    # L2
    gallons_in_pot = 6 # pot of soup has 6 gallons
    ounces_per_gallon = 128 # 128 ounces to a gallon
    total_ounces_in_pot = gallons_in_pot * ounces_per_gallon

    # L3
    time_to_serve_exact = total_ounces_in_pot / ounces_per_minute
    time_to_serve_rounded = int(time_to_serve_exact)

    # FA
    answer = time_to_serve_rounded
    return answer