def solve():
    """Index: 3616.
    Returns: the number of Asian countries Cornelia visited.
    """
    # L1
    total_countries = 42 # visited already 42 different countries
    europe_countries = 20 # 20 of them were in Europe
    south_america_countries = 10 # and 10 in South America
    remaining_countries = total_countries - europe_countries - south_america_countries

    # L2
    half_divisor = 2 # only half of them were in Asia
    asian_countries = remaining_countries / half_divisor

    # FA
    answer = asian_countries
    return answer