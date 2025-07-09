def solve(
    num_boxes: int = 10,  # Arnel had ten boxes of pencils
    pencils_kept: int = 10,  # He kept ten pencils
    num_friends: int = 5,  # shared with his five friends
    pencils_per_friend: int = 8  # his friends got eight pencils each
):
    """Index: 52.
    Returns: the number of pencils in each box.
    """
    #: L1
    total_shared_pencils = num_friends * pencils_per_friend

    #: L2
    total_pencils = pencils_kept + total_shared_pencils

    #: L3
    pencils_per_box = total_pencils / num_boxes

    answer = pencils_per_box  # FINAL ANSWER
    return answer