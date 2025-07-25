def solve():
    """Index: 6278.
    Returns: the total number of pies Milton sold during the weekend.
    """
    # L1
    customers_apple_pie = 56 # 56 customers ordered apple pie slices
    apple_pie_slices_per_pie = 8 # He cuts the apple pie into 8 slices
    apple_pies_sold = customers_apple_pie / apple_pie_slices_per_pie

    # L2
    customers_peach_pie = 48 # 48 customers ordered peach pie slices
    peach_pie_slices_per_pie = 6 # He cuts the peach pie into 6 slices
    peach_pies_sold = customers_peach_pie / peach_pie_slices_per_pie

    # L3
    total_pies_sold = apple_pies_sold + peach_pies_sold

    # FA
    answer = total_pies_sold
    return answer