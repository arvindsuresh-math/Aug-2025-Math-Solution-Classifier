def solve():
    """Index: 876.
    Returns: the number of people who joined in the final third verse.
    """
    # L1
    total_singers = 30 # 30 singers
    first_verse_divisor = 2 # half of them sang
    singers_first_verse = total_singers / first_verse_divisor

    # L2
    remaining_after_first_verse = total_singers - singers_first_verse # remaining singers
    second_verse_divisor = 3 # a third of the remaining singers
    singers_second_verse = remaining_after_first_verse / second_verse_divisor

    # L3
    singers_third_verse = total_singers - singers_first_verse - singers_second_verse

    # FA
    answer = singers_third_verse
    return answer