def solve():
    """Index: 6117.
    Returns: the number of shark sightings Cape May has.
    """
    # L6
    total_sightings = 40 # Cape May and Daytona Beach have 40 shark sightings a year
    double_factor = 2 # double the number
    less_than_double = 8 # 8 less than double
    # The problem sets up the equation: x + (2x - 8) = 40
    # This simplifies to 3x - 8 = 40, then 3x = 48, so x = 48 / 3
    daytona_sightings = (total_sightings + less_than_double) / (1 + double_factor)

    # L7
    cape_may_sightings = double_factor * daytona_sightings - less_than_double

    # FA
    answer = cape_may_sightings
    return answer