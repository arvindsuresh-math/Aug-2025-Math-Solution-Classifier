def solve(
        num_boxes: int = 10, # ten boxes of pencils
        pencils_kept_by_arnel: int = 10, # He kept ten pencils
        num_friends: int = 5, # his five friends
        pencils_per_friend: int = 8 # friends got eight pencils each
    ):
    """Index: 52.
    Returns: the number of pencils in each box.
    """
    #: L1
    pencils_shared_with_friends = num_friends * pencils_per_friend

    #: L2
    total_pencils_arnel_had = pencils_kept_by_arnel + pencils_shared_with_friends

    #: L3
    pencils_in_each_box = total_pencils_arnel_had / num_boxes

    answer = pencils_in_each_box # FINAL ANSWER
    return answer