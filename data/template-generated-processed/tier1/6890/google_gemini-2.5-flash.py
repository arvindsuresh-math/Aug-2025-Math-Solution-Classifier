def solve():
    """Index: 6890.
    Returns: how many inches longer June's sword is than Christopher's sword.
    """
    # L1
    christopher_sword_length = 15 # Christopher's sword is 15 inches long
    multiplier_twice = 2 # twice the length
    twice_christopher_length = christopher_sword_length * multiplier_twice

    # L2
    jameson_longer_than_twice_christopher = 3 # 3 inches longer than twice the length of Christopher's sword
    jameson_sword_length = twice_christopher_length + jameson_longer_than_twice_christopher

    # L3
    june_longer_than_jameson = 5 # 5 inches longer than Jameson's sword
    june_sword_length = jameson_sword_length + june_longer_than_jameson

    # L4
    june_longer_than_christopher = june_sword_length - christopher_sword_length

    # FA
    answer = june_longer_than_christopher
    return answer