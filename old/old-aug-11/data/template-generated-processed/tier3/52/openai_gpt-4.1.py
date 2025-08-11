def solve():
    """Index: 52.
    Returns: the number of pencils in each box.
    """
    # L1
    number_of_friends = 5 # his five friends
    pencils_per_friend = 8 # friends got eight pencils each
    pencils_shared = number_of_friends * pencils_per_friend

    # L2
    pencils_kept = 10 # he kept ten pencils
    total_pencils = pencils_kept + pencils_shared

    # L3
    number_of_boxes = 10 # ten boxes of pencils
    pencils_per_box = total_pencils / number_of_boxes

    # FA
    answer = pencils_per_box
    return answer