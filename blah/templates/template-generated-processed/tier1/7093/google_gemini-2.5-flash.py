def solve():
    """Index: 7093.
    Returns: the total ounces of punch Carl needs to buy for the party.
    """
    # L1
    guests = 15 # inviting 15 guests
    carl_himself = 1 # including himself
    total_people = guests + carl_himself

    # L2
    glasses_per_person = 2 # at least 2 glasses of punch
    ounces_per_glass = 12 # Each glass holds 12 ounces of punch
    ounces_per_person = glasses_per_person * ounces_per_glass

    # L3
    total_ounces_needed = total_people * ounces_per_person

    # FA
    answer = total_ounces_needed
    return answer