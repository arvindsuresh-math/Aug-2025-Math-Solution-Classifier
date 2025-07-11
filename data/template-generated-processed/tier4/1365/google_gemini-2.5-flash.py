def solve():
    """Index: 1365.
    Returns: the number of 200-kilobyte videos the drive can store.
    """
    # L1
    photo_size_kb = 1.5 # Each photo is 1.5 kilobytes in size
    max_photos = 2000 # store 2000 photos
    total_storage_kb = photo_size_kb * max_photos

    # L2
    current_photos = 400 # already has 400 photos on it
    taken_storage_kb = photo_size_kb * current_photos

    # L3
    remaining_storage_kb = total_storage_kb - taken_storage_kb

    # L4
    video_size_kb = 200 # 200-kilobyte videos
    num_videos_stored = remaining_storage_kb / video_size_kb

    # FA
    answer = num_videos_stored
    return answer