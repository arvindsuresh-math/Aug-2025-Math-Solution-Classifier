def solve():
    """Index: 6918.
    Returns: the total number of texts sent by Jennifer's boyfriend.
    """
    # L1
    grocery_texts = 5 # 5 texts about the grocery shopping
    times_more_factor = 5 # 5 times more texts
    asking_texts = grocery_texts * times_more_factor

    # L2
    texts_before_police_threat = asking_texts + grocery_texts

    # L3
    police_texts_percentage = 10 # 10% of all the texts
    percent_factor = 0.01 # WK
    police_texts = texts_before_police_threat * police_texts_percentage * percent_factor

    # L4
    total_texts = police_texts + texts_before_police_threat

    # FA
    answer = total_texts
    return answer