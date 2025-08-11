from fractions import Fraction

def solve():
    """Index: 6862.
    Returns: the amount each band member got from the concert.
    """
    # L1
    ticket_price = 30 # each ticket costs $30
    attendees = 500 # Five hundred people attended the band concert
    total_earnings = ticket_price * attendees

    # L2
    band_percentage = Fraction(70, 100) # the band gets 70% of the ticket price
    band_share = total_earnings * band_percentage

    # L3
    num_band_members = 4 # there are 4 members of the band
    each_member_share = band_share / num_band_members

    # FA
    answer = each_member_share
    return answer