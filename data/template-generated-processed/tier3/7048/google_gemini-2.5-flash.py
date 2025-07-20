def solve():
    """Index: 7048.
    Returns: the number of gigs the band has played.
    """
    # L1
    num_members = 4 # 4 members
    earnings_per_member_per_gig = 20 # $20 per gig
    band_earnings_per_gig = num_members * earnings_per_member_per_gig

    # L2
    total_earned = 400 # earned $400
    num_gigs_played = total_earned / band_earnings_per_gig

    # FA
    answer = num_gigs_played
    return answer