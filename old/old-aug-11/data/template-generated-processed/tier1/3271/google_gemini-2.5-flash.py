def solve():
    """Index: 3271.
    Returns: the total number of texts Sydney sent to Allison and Brittney on both days.
    """
    # L1
    texts_per_person_monday = 5 # sends 5 texts each to Allison and Brittney
    num_people_monday = 2 # Allison and Brittney
    total_texts_monday = texts_per_person_monday * num_people_monday

    # L2
    texts_per_person_tuesday = 15 # sends 15 texts to each of them
    num_people_tuesday = 2 # Allison and Brittney
    total_texts_tuesday = texts_per_person_tuesday * num_people_tuesday

    # L3
    total_texts_both_days = total_texts_monday + total_texts_tuesday

    # FA
    answer = total_texts_both_days
    return answer