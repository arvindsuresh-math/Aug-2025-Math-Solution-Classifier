def solve():
    """Index: 112.
    Returns: the total number of photos in the gallery after the trip.
    """
    # L1
    initial_gallery_photos = 400 # family gallery has 400 photos
    first_day_divisor = 2 # half as many photos
    first_day_photos = initial_gallery_photos / first_day_divisor

    # L2
    after_first_day_total = initial_gallery_photos + first_day_photos

    # L3
    second_day_increment = 120 # 120 more photos than first day
    second_day_photos = first_day_photos + second_day_increment

    # L4
    final_total_photos = after_first_day_total + second_day_photos

    # FA
    answer = final_total_photos
    return answer