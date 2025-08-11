def solve():
    """Index: 768.
    Returns: the total number of commencement addresses given by the three governors.
    """
    # L1
    sandoval_addresses = 12 # Governor Sandoval gave 12 commencement addresses
    hawkins_divisor = 2 # twice as many commencement addresses
    hawkins_addresses = sandoval_addresses / hawkins_divisor

    # L2
    sandoval_and_hawkins_total = hawkins_addresses + sandoval_addresses

    # L3
    sloan_additional_addresses = 10 # ten more commencement addresses
    sloan_addresses = sandoval_addresses + sloan_additional_addresses

    # L4
    total_addresses = sloan_addresses + sandoval_and_hawkins_total

    # FA
    answer = total_addresses
    return answer