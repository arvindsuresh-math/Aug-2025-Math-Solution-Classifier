def solve():
    """Index: 1916.
    Returns: the total dollars Layla earned babysitting.
    """
    # L1
    donaldsons_rate = 15 # $15 per hour for babysitting
    donaldsons_hours = 7 # Donaldsons for 7 hours
    donaldsons_earnings = donaldsons_rate * donaldsons_hours

    # L2
    merck_rate = 18 # Merck family pays $18 per hour
    merck_hours = 6 # Merck family for 6 hours
    merck_earnings = merck_rate * merck_hours

    # L3
    hille_rate = 20 # Hille family pays $20 per hour
    hille_hours = 3 # Hille family for 3 hours
    hille_earnings = hille_rate * hille_hours

    # L4
    total_earnings = donaldsons_earnings + merck_earnings + hille_earnings

    # FA
    answer = total_earnings
    return answer