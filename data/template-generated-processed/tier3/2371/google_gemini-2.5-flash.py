def solve():
    """Index: 2371.
    Returns: how many times greater the friend's area is compared to Tommy's.
    """
    # L1
    east_blocks = 3 # 3 blocks east
    west_blocks = 2 # 2 blocks west
    tommy_width = east_blocks + west_blocks

    # L2
    north_blocks = 2 # 2 blocks north
    south_blocks = 2 # 2 blocks south
    tommy_height = north_blocks + south_blocks

    # L3
    tommy_area = tommy_width * tommy_height

    # L4
    friend_area = 80 # 80 square blocks
    times_greater = friend_area / tommy_area

    # FA
    answer = times_greater
    return answer