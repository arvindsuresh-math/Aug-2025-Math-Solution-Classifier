def solve():
    """Index: 4818.
    Returns: the total number of dolls Peggy now has.
    """
    # L1
    initial_dolls = 6 # Peggy has 6 dolls
    grandmother_dolls = 30 # her grandmother gives Peggy her own collection of 30 dolls
    dolls_after_grandmother = initial_dolls + grandmother_dolls

    # L2
    half_divisor = 2 # half that amount of dolls
    holiday_dolls = grandmother_dolls / half_divisor

    # L3
    total_dolls = dolls_after_grandmother + holiday_dolls

    # FA
    answer = total_dolls
    return answer