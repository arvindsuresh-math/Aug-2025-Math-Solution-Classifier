def solve():
    """Index: 6561.
    Returns: the number of 2-foot sections Bob gets from the rope.
    """
    # L1
    total_rope_length = 50 # Bob buys 50 feet of rope
    fraction_denominator = 5 # a 5th of it
    rope_used_for_art = total_rope_length / fraction_denominator

    # L2
    rope_remaining_after_art = total_rope_length - rope_used_for_art

    # L3
    half_divisor = 2 # half of it
    rope_after_giving_to_friend = rope_remaining_after_art / half_divisor

    # L4
    section_length = 2 # 2-foot sections
    number_of_sections = rope_after_giving_to_friend / section_length

    # FA
    answer = number_of_sections
    return answer