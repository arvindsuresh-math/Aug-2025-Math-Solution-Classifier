def solve():
    """Index: 1229.
    Returns: the average height of the four people.
    """
    # L1
    zara_height = 64 # Zara is 64 inches tall
    zora_shorter_by = 8 # 8 inches shorter than Brixton
    zora_height = zara_height - zora_shorter_by

    # L2
    brixton_height = zara_height # has the same height as Brixton
    zara_brixton_total_height = zara_height + brixton_height

    # L3
    three_people_total_height = zara_brixton_total_height + zora_height

    # L4
    itzayana_taller_by = 4 # Itzayana is 4 inches taller than Zora
    itzayana_height = zora_height + itzayana_taller_by

    # L5
    four_friends_total_height = itzayana_height + three_people_total_height

    # L6
    number_of_people = 4 # four people
    average_height = four_friends_total_height / number_of_people

    # FA
    answer = average_height
    return answer