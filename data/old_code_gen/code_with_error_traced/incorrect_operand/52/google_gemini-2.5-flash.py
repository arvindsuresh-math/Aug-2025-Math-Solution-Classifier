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
    pencils_shared_with_friends = num_friends * pencils_per_friend # eval: 40 = 5 * 8

    #: L2
    total_pencils_arnel_had = pencils_shared_with_friends + pencils_shared_with_friends # eval: 80 = 40 + 40

    #: L3
    pencils_per_box = total_pencils_arnel_had / num_boxes # eval: 8.0 = 80 / 10

    #: FA
    answer = pencils_per_box
    return answer # eval: return 8.0
