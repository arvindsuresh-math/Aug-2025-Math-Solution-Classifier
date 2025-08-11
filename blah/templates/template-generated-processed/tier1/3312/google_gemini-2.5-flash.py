def solve():
    """Index: 3312.
    Returns: the total amount paid per episode.
    """
    # L1
    minor_character_pay_per_episode = 15000 # minor characters $15,000 each episode
    num_minor_characters = 4 # 4 minor characters
    total_minor_character_pay = minor_character_pay_per_episode * num_minor_characters

    # L2
    major_character_pay_multiplier = 3 # three times as much
    major_character_pay_per_character = minor_character_pay_per_episode * major_character_pay_multiplier

    # L3
    num_main_characters = 5 # 5 main characters
    total_main_character_pay = major_character_pay_per_character * num_main_characters

    # L4
    total_pay_per_episode = total_main_character_pay + total_minor_character_pay

    # FA
    answer = total_pay_per_episode
    return answer