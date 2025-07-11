def solve():
    """Index: 306.
    Returns: the average height of Parker, Daisy, and Reese in inches.
    """
    # L1
    reese_height = 60 # Reese is 60 inches tall
    daisy_taller_than_reese = 8 # Daisy is 8 inches taller than Reese
    daisy_height = reese_height + daisy_taller_than_reese

    # L2
    parker_shorter_than_daisy = 4 # Parker is 4 inches shorter than Daisy
    parker_height = daisy_height - parker_shorter_than_daisy

    # L3
    number_of_people = 3 # WK
    average_height = (reese_height + daisy_height + parker_height) / number_of_people

    # FA
    answer = average_height
    return answer