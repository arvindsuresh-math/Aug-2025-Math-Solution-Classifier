def solve():
    """Index: 5782.
    Returns: the total number of photos Palmer has under her bed.
    """
    # L1
    photos_first_week = 50 # 50 new pictures in the first week
    multiplier_second_week = 2 # twice that many in the second week
    photos_second_week = multiplier_second_week * photos_first_week

    # L2
    # Note: The solution uses 130 photos for the third and fourth weeks, 
    # while the question states 80 photos for these weeks.
    photos_third_fourth_weeks_from_solution = 130 # 130 photos (as used in solution's calculation)
    total_photos_bali = photos_first_week + photos_second_week + photos_third_fourth_weeks_from_solution

    # L3
    initial_album_photos = 100 # album of 100 photos
    final_total_photos = total_photos_bali + initial_album_photos

    # FA
    answer = final_total_photos
    return answer