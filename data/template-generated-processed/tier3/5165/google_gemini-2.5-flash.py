def solve():
    """Index: 5165.
    Returns: the total time Gwendolyn will take to read the book in hours.
    """
    # L1
    paragraphs_per_page = 20 # 20 paragraphs per page
    total_pages = 50 # the book has 50 pages
    total_paragraphs = total_pages * paragraphs_per_page

    # L2
    sentences_per_paragraph = 10 # each paragraph has 10 sentences
    total_sentences = total_paragraphs * sentences_per_paragraph

    # L3
    sentences_per_hour = 200 # read 200 sentences of a book in 1 hour
    total_reading_time_hours = total_sentences / sentences_per_hour

    # FA
    answer = total_reading_time_hours
    return answer