def solve():
    """Index: 5012.
    Returns: the total number of outfits Carlton has.
    """
    # L1
    multiplier_for_vests = 2 # twice as many sweater vests
    button_up_shirts = 3 # three button-up shirts
    sweater_vests = multiplier_for_vests * button_up_shirts

    # L2
    total_outfits = button_up_shirts * sweater_vests

    # FA
    answer = total_outfits
    return answer