def solve():
    """Index: 2191.
    Returns: the total amount Mary spent on soft drinks.
    """
    # L1
    more_girls = 10 # 10 more girls
    males = 15 # 15 males
    girls = more_girls + males

    # L2
    total_attendees = males + girls

    # L3
    cans_per_attendee = 2 # Each attendee received 2 cans of soft drinks
    total_cans_needed = total_attendees * cans_per_attendee

    # L4
    cans_per_box = 8 # a box contains 8 cans
    boxes_bought = total_cans_needed / cans_per_box

    # L5
    price_per_box = 5 # is priced at $5 for each box
    total_cost = boxes_bought * price_per_box

    # FA
    answer = total_cost
    return answer