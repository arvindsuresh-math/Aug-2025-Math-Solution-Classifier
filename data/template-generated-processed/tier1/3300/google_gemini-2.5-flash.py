def solve():
    """Index: 3300.
    Returns: the number of riddles Taso has.
    """
    # L1
    josh_riddles = 8 # Josh has 8 riddles
    ivory_more_than_josh = 4 # four more riddles than Josh did
    ivory_riddles = josh_riddles + ivory_more_than_josh

    # L2
    taso_multiplier = 2 # twice as many riddles as Ivory did
    taso_riddles = ivory_riddles * taso_multiplier

    # FA
    answer = taso_riddles
    return answer