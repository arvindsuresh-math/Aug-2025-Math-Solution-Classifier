def solve():
    """Index: 6984.
    Returns: the number of words they should add to reach the research paper requirement.
    """
    # L1
    yvonne_words = 400 # Yvonne was able to write 400 words
    janna_more_than_yvonne = 150 # Janna wrote 150 more words than Yvonne
    janna_words = yvonne_words + janna_more_than_yvonne

    # L2
    total_words_initial = yvonne_words + janna_words

    # L3
    words_removed = 20 # removed 20 words
    words_after_removal = total_words_initial - words_removed

    # L4
    multiplier_added_words = 2 # added twice as many words as they removed
    words_added = words_removed * multiplier_added_words

    # L5
    current_total_words = words_after_removal + words_added

    # L6
    paper_requirement = 1000 # 1000-word pair research paper
    words_to_add = paper_requirement - current_total_words

    # FA
    answer = words_to_add
    return answer