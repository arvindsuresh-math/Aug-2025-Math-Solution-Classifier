def solve():
    """Index: 4665.
    Returns: the number of trackball mice sold.
    """
    # L1
    total_mice_sold = 80 # sell a total of 80 mice
    wireless_mice_denominator = 2 # half of their sales are wireless mice
    wireless_mice_sold = total_mice_sold / wireless_mice_denominator

    # L2
    optical_mice_denominator = 4 # one-fourth are optical mice
    optical_mice_sold = total_mice_sold / optical_mice_denominator

    # L3
    total_wireless_optical_mice = wireless_mice_sold + optical_mice_sold

    # L4
    trackball_mice_sold = total_mice_sold - total_wireless_optical_mice

    # FA
    answer = trackball_mice_sold
    return answer