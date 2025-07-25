def solve():
    """Index: 6361.
    Returns: the number of pages Sam read.
    """
    # L1
    assigned_pages = 25 # minimum of 25 pages of reading
    harrison_more_than_assigned = 10 # Harrison read 10 more pages than assigned
    harrison_pages = harrison_more_than_assigned + assigned_pages

    # L2
    pam_more_than_harrison = 15 # Pam read 15 more pages than Harrison
    pam_pages = pam_more_than_harrison + harrison_pages

    # L3
    sam_multiplier = 2 # Sam read twice the amount of Pam
    sam_pages = sam_multiplier * pam_pages

    # FA
    answer = sam_pages
    return answer