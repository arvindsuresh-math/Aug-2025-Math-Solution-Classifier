def solve():
    """Index: 1365.
    Returns: the number of 200-kilobyte videos the drive can store with 400 photos already on it.
    """
    # L1
    photo_size_kb = 1.5 # Each photo is 1.5 kilobytes in size
    max_photos = 2000 # enough kilobytes of storage space to store 2000 photos
    total_storage_kb = photo_size_kb * max_photos

    # L2
    used_photos = 400 # already has 400 photos on it
    used_storage_kb = photo_size_kb * used_photos

    # L3
    remaining_storage_kb = total_storage_kb - used_storage_kb

    # L4
    video_size_kb = 200 # 200-kilobyte videos
    num_videos = remaining_storage_kb / video_size_kb

    # FA
    answer = num_videos
    return answer