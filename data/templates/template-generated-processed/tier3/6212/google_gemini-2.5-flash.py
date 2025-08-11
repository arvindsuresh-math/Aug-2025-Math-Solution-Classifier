def solve():
    """Index: 6212.
    Returns: the total number of stuffed bears Eden has now.
    """
    # L1
    total_bears = 20 # 20 stuffed bears
    favorite_bears = 8 # her favorite 8 bears
    remaining_bears = total_bears - favorite_bears

    # L2
    num_sisters = 3 # her 3 sisters
    bears_per_sister = remaining_bears / num_sisters

    # L3
    eden_initial_bears = 10 # Eden, already had 10 stuffed bears
    eden_total_bears = eden_initial_bears + bears_per_sister

    # FA
    answer = eden_total_bears
    return answer