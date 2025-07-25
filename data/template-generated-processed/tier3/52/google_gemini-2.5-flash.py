def solve():
    """Index: 52.
    Returns: the number of pencils in each box.
    """
    # L1
    num_friends = 5 # shared the remaining pencils equally with his five friends
    pencils_per_friend = 8 # If his friends got eight pencils each
    pencils_shared_with_friends = num_friends * pencils_per_friend

    # L2
    pencils_kept = 10 # He kept ten pencils
    total_pencils_arnel_had = pencils_kept + pencils_shared_with_friends

    # L3
    num_boxes = 10 # ten boxes of pencils
    pencils_per_box = total_pencils_arnel_had / num_boxes

    # FA
    answer = pencils_per_box
    return answer