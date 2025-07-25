def solve():
    """Index: 4106.
    Returns: the total number of cans collected by the boys.
    """
    # L1
    solomon_cans = 66 # Solomon collected 66 cans
    solomon_juwan_ratio = 3 # three times as many cans as Juwan
    juwan_cans = solomon_cans / solomon_juwan_ratio

    # L2
    levi_subtraction_value = 11 # WK
    levi_cans = juwan_cans - levi_subtraction_value

    # L3
    total_cans = solomon_cans + juwan_cans + levi_cans

    # FA
    answer = total_cans
    return answer