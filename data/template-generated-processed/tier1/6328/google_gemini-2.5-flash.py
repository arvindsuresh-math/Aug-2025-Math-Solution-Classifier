def solve():
    """Index: 6328.
    Returns: the total cost for both suits.
    """
    # L1
    off_the_rack_suit_cost = 300 # The first is an off-the-rack suit which costs $300.
    multiplier_tailored_suit = 3 # costs three as much
    second_suit_base_cost = off_the_rack_suit_cost * multiplier_tailored_suit

    # L2
    tailoring_cost = 200 # plus an extra $200 for tailoring
    second_suit_total_cost = second_suit_base_cost + tailoring_cost

    # L3
    total_cost = second_suit_total_cost + off_the_rack_suit_cost

    # FA
    answer = total_cost
    return answer