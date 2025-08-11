def solve():
    """Index: 229.
    Returns: the number of cable sections Jan keeps on hand.
    """
    # L1
    total_cable_feet = 1000 # Jan buys 1000 feet of cable
    section_length = 25 # 25-foot sections
    total_sections = total_cable_feet / section_length

    # L2
    friend_share_denominator = 4 # 1/4 of that to a friend
    sections_given_to_friend = total_sections / friend_share_denominator

    # L3
    sections_after_giving_to_friend = total_sections - sections_given_to_friend

    # L4
    storage_share_denominator = 2 # half of the rest in storage
    sections_on_hand = sections_after_giving_to_friend / storage_share_denominator

    # FA
    answer = sections_on_hand
    return answer