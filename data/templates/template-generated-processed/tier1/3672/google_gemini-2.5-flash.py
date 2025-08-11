def solve():
    """Index: 3672.
    Returns: the total number of words in the poem.
    """
    # L1
    words_per_line = 8 # each line has 8 words
    lines_per_stanza = 10 # each stanza has 10 lines
    words_per_stanza = words_per_line * lines_per_stanza

    # L2
    total_stanzas = 20 # 20 stanzas
    total_words_in_poem = words_per_stanza * total_stanzas

    # FA
    answer = total_words_in_poem
    return answer