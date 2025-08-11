def solve():
    """Index: 5520.
    Returns: the total amount John spent.
    """
    # L1
    computer_cost = 1500 # John's new computer cost $1500
    peripherals_divisor = 5 # 1/5 that much
    peripherals_cost = computer_cost / peripherals_divisor

    # L2
    base_video_card_cost = 300 # the $300 video card
    upgrade_multiplier = 2 # twice as much
    upgraded_video_card_cost = base_video_card_cost * upgrade_multiplier

    # L3
    additional_video_card_cost = upgraded_video_card_cost - base_video_card_cost

    # L4
    total_cost = computer_cost + peripherals_cost + additional_video_card_cost

    # FA
    answer = total_cost
    return answer