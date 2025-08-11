def solve():
    """Index: 3555.
    Returns: how many more pens Alex will have than Jane after a month.
    """
    # L1
    alex_pens_week1 = 4 # Alex has 4 pens in the first week
    doubling_factor = 2 # pen collection doubles
    alex_pens_week2 = alex_pens_week1 * doubling_factor

    # L2
    alex_pens_week3 = doubling_factor * alex_pens_week2

    # L3
    alex_pens_week4 = doubling_factor * alex_pens_week3

    # L4
    jane_pens_after_month = 16 # Jane will have 16 pens after a month
    alex_more_than_jane = alex_pens_week4 - jane_pens_after_month

    # FA
    answer = alex_more_than_jane
    return answer