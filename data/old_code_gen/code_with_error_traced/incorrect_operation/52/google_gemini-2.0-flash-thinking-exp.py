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
    pencils_shared = num_friends + pencils_per_friend # eval: 13 = 5 + 8

    #: L2
    total_pencils = pencils_kept + pencils_shared # eval: 23 = 10 + 13

    #: L3
    pencils_in_each_box = total_pencils / num_boxes # eval: 2.3 = 23 / 10

    #: FA
    answer = pencils_in_each_box
    return answer # eval: return 2.3
