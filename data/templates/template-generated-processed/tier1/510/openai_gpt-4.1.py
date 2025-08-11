def solve():
    """Index: 510.
    Returns: the total money the pie shop will earn from selling all custard pie slices.
    """
    # L1
    num_whole_pies = 6 # 6 whole custard pies
    slices_per_pie = 10 # each whole pie into 10 slices
    total_slices = num_whole_pies * slices_per_pie

    # L2
    price_per_slice = 3 # $3 per slice of custard pie
    total_earnings = price_per_slice * total_slices

    # FA
    answer = total_earnings
    return answer