def solve():
    """Index: 1234.
    Returns: the number of pistachios with shells and opened shells.
    """
    # L1
    total_pistachios = 80 # A bag of pistachios has 80 pistachios in it
    percent_with_shells = 0.95 # 95 percent have shells
    pistachios_with_shells = total_pistachios * percent_with_shells

    # L2
    percent_opened_shells = 0.75 # 75 percent of those have shells that are opened
    pistachios_with_opened_shells = pistachios_with_shells * percent_opened_shells

    # FA
    answer = pistachios_with_opened_shells
    return answer