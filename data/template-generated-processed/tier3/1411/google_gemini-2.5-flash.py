def solve():
    """Index: 1411.
    Returns: the number of words Lucas has left to write.
    """
    # L1
    lines_per_page = 20 # 20 lines fit on each page
    half_page_divisor = 2 # Half a page is 20 / 2
    half_page_lines = lines_per_page / half_page_divisor

    # L2
    full_pages_written_lines = 20 # one and a half pages -> one full page has 20 lines
    total_lines_written = full_pages_written_lines + half_page_lines

    # L3
    words_per_line = 10 # 10 words fit on each line
    total_words_written = total_lines_written * words_per_line

    # L4
    total_story_words = 400 # a 400-word story
    words_left_to_write = total_story_words - total_words_written

    # FA
    answer = words_left_to_write
    return answer