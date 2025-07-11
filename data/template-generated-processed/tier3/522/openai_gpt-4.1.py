def solve():
    """Index: 522.
    Returns: the number of barnyard owls making the noise.
    """
    # L1
    total_hoots_per_minute = 20 # 20 hoots per minute
    hoots_less = 5 # 5 less than 20 hoots per minute
    heard_hoots_per_minute = total_hoots_per_minute - hoots_less

    # L2
    hoots_per_owl = 5 # one barnyard owl makes 5 hoot sounds per minute
    number_of_owls = heard_hoots_per_minute / hoots_per_owl

    # FA
    answer = number_of_owls
    return answer