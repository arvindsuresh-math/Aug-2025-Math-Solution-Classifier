def solve():
    """Index: 5775.
    Returns: the number of vehicles that can still park.
    """
    # L1
    num_caravans = 3 # 3 caravans currently parking
    spaces_per_caravan = 2 # A caravan takes up a total of 2 spaces of parking space
    spaces_used_by_caravans = num_caravans * spaces_per_caravan

    # L2
    total_spaces = 30 # 30 spaces for each vehicle in a parking lot
    remaining_spaces = total_spaces - spaces_used_by_caravans

    # FA
    answer = remaining_spaces
    return answer