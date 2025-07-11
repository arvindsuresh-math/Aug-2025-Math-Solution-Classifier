def solve():
    """Index: 2365.
    Returns: the year the archaeologist dated the second dig site.
    """
    # L1
    fourth_site_date_bc = 8400 # The fourth dig site’s relics and gave the site a date of 8400 BC
    twice_as_old_divisor = 2 # The fourth dig site was twice as old as the third dig site
    third_site_date_bc = fourth_site_date_bc / twice_as_old_divisor

    # L2
    older_than_first_site = 3700 # The third dig site was dated 3700 years older than the first dig site
    first_site_date_bc = third_site_date_bc - older_than_first_site

    # L3
    more_recent_than_second_site = 352 # The archaeologist dated the first dig site as 352 years more recent than the second dig site
    second_site_date_bc = first_site_date_bc + more_recent_than_second_site

    # FA
    answer = second_site_date_bc
    return answer