def solve():
    """Index: 5112.
    Returns: the duration in days a notepad would last.
    """
    # L1
    pieces_per_fold_factor = 2 # WK
    pieces_per_letter_paper = pieces_per_fold_factor * pieces_per_fold_factor * pieces_per_fold_factor

    # L2
    num_letter_papers = 5 # 5 pieces of letter-size paper
    total_note_papers = num_letter_papers * pieces_per_letter_paper

    # L3
    notes_per_day = 10 # wrote 10 notes per day
    notepad_duration_days = total_note_papers / notes_per_day

    # FA
    answer = notepad_duration_days
    return answer