def solve():
    """Index: 1292.
    Returns: the total number of fireworks lit during the display.
    """
    # L1
    num_digits_year = 4 # show the full year
    fireworks_per_number = 6 # 6 fireworks to display a number
    fireworks_for_year = num_digits_year * fireworks_per_number

    # L2
    num_letters_happy_new_year = 12 # “HAPPY NEW YEAR” contains 12 letters
    fireworks_per_letter = 5 # 5 fireworks to display a letter
    fireworks_for_phrase = num_letters_happy_new_year * fireworks_per_letter

    # L3
    initial_fireworks_total = fireworks_for_year + fireworks_for_phrase

    # L4
    num_boxes = 50 # another 50 boxes of fireworks
    fireworks_per_box = 8 # Each box of fireworks contains 8 fireworks
    fireworks_from_boxes = num_boxes * fireworks_per_box

    # L5
    total_fireworks_display = initial_fireworks_total + fireworks_from_boxes

    # FA
    answer = total_fireworks_display
    return answer