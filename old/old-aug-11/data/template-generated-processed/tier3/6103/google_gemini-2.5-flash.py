def solve():
    """Index: 6103.
    Returns: the total number of soda cans Tim has in the end.
    """
    # L1
    initial_cans = 22 # Tim has 22 cans of soda
    cans_taken_by_jeff = 6 # takes 6 cans of soda from Tim
    cans_after_jeff = initial_cans - cans_taken_by_jeff

    # L2
    half_amount_divisor = 2 # another half the amount of soda cans
    cans_bought = cans_after_jeff / half_amount_divisor

    # L3
    total_cans = cans_after_jeff + cans_bought

    # FA
    answer = total_cans
    return answer