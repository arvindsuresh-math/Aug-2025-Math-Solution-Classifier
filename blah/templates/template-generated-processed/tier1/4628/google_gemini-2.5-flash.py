def solve():
    """Index: 4628.
    Returns: the total number of letters the three received.
    """
    # L1
    brother_letters = 40 # Greta's brother received 40 letters
    greta_more_than_brother = 10 # 10 more letters
    greta_letters = brother_letters + greta_more_than_brother

    # L2
    greta_and_brother_total = greta_letters + brother_letters

    # L3
    mother_multiplier = 2 # twice the total number
    mother_letters = greta_and_brother_total * mother_multiplier

    # L4
    total_letters_three = greta_and_brother_total + mother_letters

    # FA
    answer = total_letters_three
    return answer