def solve():
    """Index: 5706.
    Returns: the total number of stickers Peggy uses.
    """
    # L1
    sheets_per_folder = 10 # ten sheets of paper in each folder
    red_folder_stickers_per_sheet = 3 # In the red folder, each sheet of paper gets 3 stickers
    red_folder_total_stickers = sheets_per_folder * red_folder_stickers_per_sheet

    # L2
    green_folder_stickers_per_sheet = 2 # In the green folder, each sheet of paper gets 2 stickers
    green_folder_total_stickers = sheets_per_folder * green_folder_stickers_per_sheet

    # L3
    blue_folder_stickers_per_sheet = 1 # in the blue folder, each sheet gets 1 sticker
    blue_folder_total_stickers = sheets_per_folder * blue_folder_stickers_per_sheet

    # L4
    total_stickers_used = red_folder_total_stickers + green_folder_total_stickers + blue_folder_total_stickers

    # FA
    answer = total_stickers_used
    return answer