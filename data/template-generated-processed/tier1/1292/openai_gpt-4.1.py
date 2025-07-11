def solve():
    """Index: 1292.
    Returns: the total number of fireworks lit during the display.
    """
    # L1
    num_digits_in_year = 4 # Writing out the full year uses 4 numbers
    fireworks_per_number = 6 # 6 fireworks to display a number
    fireworks_for_year = num_digits_in_year * fireworks_per_number

    # L2
    num_letters_in_phrase = 12 # “HAPPY NEW YEAR” contains 12 letters
    fireworks_per_letter = 5 # 5 fireworks to display a letter
    fireworks_for_phrase = num_letters_in_phrase * fireworks_per_letter

    # L3
    initial_fireworks = fireworks_for_year + fireworks_for_phrase

    # L4
    num_boxes = 50 # another 50 boxes of fireworks
    fireworks_per_box = 8 # Each box of fireworks contains 8 fireworks
    fireworks_from_boxes = num_boxes * fireworks_per_box

    # L5
    total_fireworks = initial_fireworks + fireworks_from_boxes

    # FA
    answer = total_fireworks
    return answer