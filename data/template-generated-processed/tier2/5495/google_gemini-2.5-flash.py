def solve():
    """Index: 5495.
    Returns: the number of free-throws Annieka made.
    """
    # L1
    deshawn_free_throws = 12 # DeShawn made 12 free-throws
    kayla_percentage_increase = 1.50 # 50% more than DeShawn
    kayla_free_throws = deshawn_free_throws * kayla_percentage_increase

    # L2
    fewer_than_kayla = 4 # 4 fewer than Kayla
    annieka_free_throws = kayla_free_throws - fewer_than_kayla

    # FA
    answer = annieka_free_throws
    return answer