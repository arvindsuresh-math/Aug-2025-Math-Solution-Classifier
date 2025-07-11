def solve():
    """Index: 112.
    Returns: the total number of photos in the gallery.
    """
    # L1
    initial_gallery_photos = 400 # 400 photos
    half_divisor = 2 # half as many photos
    photos_day1 = initial_gallery_photos / half_divisor

    # L2
    photos_after_day1_addition = initial_gallery_photos + photos_day1

    # L3
    more_photos_day2 = 120 # 120 more photos
    photos_day2 = photos_day1 + more_photos_day2

    # L4
    total_photos_in_gallery = photos_after_day1_addition + photos_day2

    # FA
    answer = total_photos_in_gallery
    return answer