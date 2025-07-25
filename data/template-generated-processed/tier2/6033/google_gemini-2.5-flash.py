def solve():
    """Index: 6033.
    Returns: the length of the third generation's tails.
    """
    # L1
    percentage_increase_num = 25 # 25% longer
    first_generation_tail_length = 16 # tails 16 cm long
    percent_factor = 0.01 # WK
    increase_gen2 = percentage_increase_num * percent_factor * first_generation_tail_length

    # L2
    second_generation_tail_length = increase_gen2 + first_generation_tail_length

    # L3
    increase_gen3 = percentage_increase_num * percent_factor * second_generation_tail_length

    # L4
    third_generation_tail_length = increase_gen3 + second_generation_tail_length

    # FA
    answer = third_generation_tail_length
    return answer