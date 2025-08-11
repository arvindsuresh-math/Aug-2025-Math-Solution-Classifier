def solve():
    """Index: 7058.
    Returns: the total number of kids Nellie played with.
    """
    # L1
    num_sisters = 6 # 6 sisters
    num_brothers = 8 # 8 brothers
    kids_hide_and_seek = num_sisters + num_brothers

    # L2
    num_cousins = 22 # all 22 of her cousins
    total_kids = kids_hide_and_seek + num_cousins

    # FA
    answer = total_kids
    return answer