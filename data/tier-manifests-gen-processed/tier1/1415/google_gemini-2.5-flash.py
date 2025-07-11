def solve():
    """Index: 1415.
    Returns: the total money Penny makes from selling cheesecake pies.
    """
    # L1
    pies_sold = 7 # 7 cheesecake pies
    slices_per_pie = 6 # cut into 6 thick slices
    total_slices = pies_sold * slices_per_pie

    # L2
    price_per_slice = 7 # $7 a slice
    total_money = total_slices * price_per_slice

    # FA
    answer = total_money
    return answer