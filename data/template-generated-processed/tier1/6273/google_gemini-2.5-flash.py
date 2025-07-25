def solve():
    """Index: 6273.
    Returns: Stacy's current height.
    """
    # L1
    stacy_growth_more_than_brother = 6 # grew 6 inches more than her brother
    brother_growth = 1 # grew 1 inch last year
    stacy_total_growth = stacy_growth_more_than_brother + brother_growth

    # L2
    stacy_height_last_year = 50 # 50 inches tall last year
    stacy_current_height = stacy_height_last_year + stacy_total_growth

    # FA
    answer = stacy_current_height
    return answer