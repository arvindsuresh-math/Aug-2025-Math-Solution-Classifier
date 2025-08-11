def solve():
    """Index: 1724.
    Returns: the total number of stamps Parker has now.
    """
    # L1
    Addie_total_stamps = 72 # her 72 stamps
    fraction_denominator = 4 # one fourth
    stamps_addie_put_in = Addie_total_stamps / fraction_denominator

    # L2
    parker_initial_stamps = 18 # 18 stamps in Parker’s scrapbook
    parker_total_stamps = parker_initial_stamps + stamps_addie_put_in

    # FA
    answer = parker_total_stamps
    return answer