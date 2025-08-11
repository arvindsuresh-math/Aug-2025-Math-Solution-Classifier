def solve():
    """Index: 1120.
    Returns: the number of brochures the printing press is creating.
    """
    # L1
    single_page_spreads = 20 # 20 single-page spreads
    double_page_spread_multiplier = 2 # twice as many double-page spreads
    double_page_spreads = single_page_spreads * double_page_spread_multiplier

    # L2
    pages_per_double_spread = 2 # double-page spreads are made up of 2 pages each
    double_page_spread_pages = double_page_spreads * pages_per_double_spread

    # L3
    total_spread_pages = single_page_spreads + double_page_spread_pages

    # L4
    pages_per_block = 4 # a block of ads is printed every 4 pages
    num_blocks = total_spread_pages / pages_per_block

    # L5
    ads_per_block = 4 # 4 ads per block
    total_ads = num_blocks * ads_per_block

    # L6
    ad_page_fraction = 0.25 # each ad takes up a quarter of a page
    ad_pages = total_ads * ad_page_fraction

    # L7
    total_pages = total_spread_pages + ad_pages

    # L8
    pages_per_brochure = 5 # brochures are made up of 5 pages each
    num_brochures = total_pages / pages_per_brochure

    # FA
    answer = num_brochures
    return answer