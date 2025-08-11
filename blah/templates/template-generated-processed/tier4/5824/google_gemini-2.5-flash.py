def solve():
    """Index: 5824.
    Returns: the total number of dimes Dan has.
    """
    # L1
    barry_total_value = 10.00 # $10.00 worth of dimes
    dime_value = 0.10 # WK
    barry_num_dimes = barry_total_value / dime_value

    # L2
    dan_half_divisor = 2 # half that amount
    dan_initial_dimes = barry_num_dimes / dan_half_divisor

    # L3
    dan_found_dimes = 2 # finds 2 more dimes
    dan_total_dimes = dan_initial_dimes + dan_found_dimes

    # FA
    answer = dan_total_dimes
    return answer