def solve():
    """Index: 2010.
    Returns: the total amount of water Stan needs to drink.
    """
    # L1
    num_pages = 5 # 5-page paper
    words_per_page = 400 # Each page will contain 400 words
    total_words_to_write = num_pages * words_per_page

    # L2
    typing_speed = 50 # 50 words per minute
    time_to_type_minutes = total_words_to_write / typing_speed

    # L3
    water_per_hour = 15 # drink 15 ounces of water
    minutes_per_hour = 60 # WK
    water_per_minute = water_per_hour / minutes_per_hour

    # L4
    total_water_needed = time_to_type_minutes * water_per_minute

    # FA
    answer = total_water_needed
    return answer