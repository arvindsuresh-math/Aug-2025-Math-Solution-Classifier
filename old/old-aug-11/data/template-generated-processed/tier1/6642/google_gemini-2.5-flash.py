def solve():
    """Index: 6642.
    Returns: the total number of channels Larry has.
    """
    # L1
    initial_channels = 150 # 150 channels
    channels_taken_away_1 = 20 # took 20 channels away
    channels_added_1 = 12 # replaced those with 12 channels
    channels_after_first_change = initial_channels - channels_taken_away_1 + channels_added_1

    # L2
    channels_reduced_2 = 10 # reduce his package by 10 more channels
    sports_package_added_1 = 8 # add the sports package which is 8 channels
    channels_after_second_change = channels_after_first_change - channels_reduced_2 + sports_package_added_1

    # L3
    supreme_sports_package_added = 7 # that package adds 7 more channels
    final_channels = channels_after_second_change + supreme_sports_package_added

    # FA
    answer = final_channels
    return answer