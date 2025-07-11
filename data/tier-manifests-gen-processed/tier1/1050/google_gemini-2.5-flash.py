def solve():
    """Index: 1050.
    Returns: the number of photos Tom has.
    """
    # L1
    total_photos = 152 # total amount of photos which is 152
    tim_less_than_total = 100 # one hundred photos less than the total amount
    tim_photos = total_photos - tim_less_than_total

    # L2
    paul_more_than_tim = 10 # 10 photos more than Tim
    paul_photos = tim_photos + paul_more_than_tim

    # L3
    tim_and_paul_total = tim_photos + paul_photos

    # L4
    tom_photos = total_photos - tim_and_paul_total

    # FA
    answer = tom_photos
    return answer