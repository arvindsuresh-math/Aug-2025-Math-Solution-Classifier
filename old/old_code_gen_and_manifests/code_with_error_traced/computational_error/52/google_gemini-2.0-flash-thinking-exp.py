def solve(
    num_boxes: int = 10, # ten boxes of pencils
    pencils_kept: int = 10, # He kept ten pencils
    num_friends: int = 5, # shared the remaining pencils equally with his five friends
    pencils_per_friend: int = 8 # his friends got eight pencils each
):
    """Index: 52.
    Returns: the number of pencils in each box.
    """

    #: L1
    pencils_shared = num_friends * pencils_per_friend # eval: 40 = 5 * 8

    #: L2
    total_pencils = pencils_kept + pencils_shared # eval: 50 = 10 + 40

    #: L3
    pencils_in_each_box = -5.0 # eval: -5.0 = -5.0

    #: FA
    answer = pencils_in_each_box
    return answer # eval: return -5.0
