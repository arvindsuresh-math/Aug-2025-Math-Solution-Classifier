def solve():
    """Index: 1120.
    Returns: the total number of brochures the printing press is creating.
    """
    # L1
    single_page_spreads = 20 # 20 single-page spreads
    double_spread_multiplier = 2 # twice as many double-page spreads
    double_page_spreads = single_page_spreads * double_spread_multiplier

    # L2
    pages_per_double_spread = 2 # made up of 2 pages each
    pages_from_double_spreads = double_page_spreads * pages_per_double_spread

    # L3
    total_pages_from_spreads = single_page_spreads + pages_from_double_spreads

    # L4
    pages_per_ad_block = 4 # For each 4 pages printed for the spreads
    num_ad_blocks = total_pages_from_spreads / pages_per_ad_block

    # L5
    ads_per_block = 4 # a block of 4 ads
    total_ads = num_ad_blocks * ads_per_block

    # L6
    pages_per_ad = 0.25 # a quarter of a page
    pages_from_ads = total_ads * pages_per_ad

    # L7
    total_pages_printed = total_pages_from_spreads + pages_from_ads

    # L8
    pages_per_brochure = 5 # made up of 5 pages each
    num_brochures = total_pages_printed / pages_per_brochure

    # FA
    answer = num_brochures
    return answer