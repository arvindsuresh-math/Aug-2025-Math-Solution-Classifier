def solve():
    """Index: 6029.
    Returns: the amount of concrete needed for the supporting pillars.
    """
    # L1
    concrete_one_anchor = 700 # using 700 tons of concrete
    num_anchors = 2 # The two bridge anchors
    total_anchor_concrete = concrete_one_anchor * num_anchors

    # L2
    roadway_deck_concrete = 1600 # needs 1600 tons of concrete
    concrete_deck_and_anchors = roadway_deck_concrete + total_anchor_concrete

    # L3
    total_bridge_concrete = 4800 # total amount of concrete in the entire bridge will be 4800 tons
    pillars_concrete = total_bridge_concrete - concrete_deck_and_anchors

    # FA
    answer = pillars_concrete
    return answer