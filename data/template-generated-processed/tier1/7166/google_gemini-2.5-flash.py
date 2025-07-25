def solve():
    """Index: 7166.
    Returns: the combined number of degrees Summer and Jolly have.
    """
    # L1
    summer_degrees = 150 # Summer has a total of 150 degrees
    summer_more_than_jolly = 5 # Summer had five more degrees than Jolly
    jolly_degrees = summer_degrees - summer_more_than_jolly

    # L2
    combined_degrees = summer_degrees + jolly_degrees

    # FA
    answer = combined_degrees
    return answer