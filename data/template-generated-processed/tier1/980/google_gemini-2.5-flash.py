def solve():
    """Index: 980.
    Returns: the total number of corn cobs the farm has grown.
    """
    # L1
    rows_field1 = 13 # 13 full rows of corn cobs
    cobs_per_row = 4 # 4 corn cobs
    cobs_in_field1 = rows_field1 * cobs_per_row

    # L2
    rows_field2 = 16 # 16 full rows of corn cobs
    cobs_in_field2 = rows_field2 * cobs_per_row

    # L3
    total_corn_cobs = cobs_in_field1 + cobs_in_field2

    # FA
    answer = total_corn_cobs
    return answer