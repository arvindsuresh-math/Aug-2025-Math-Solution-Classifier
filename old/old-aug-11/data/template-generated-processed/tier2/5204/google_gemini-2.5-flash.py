def solve():
    """Index: 5204.
    Returns: the total time spent on exploring, notes, and book writing.
    """
    # L1
    exploration_years = 3 # spent 3 years of his life exploring the jungle
    half_factor = 0.5 # half as much time
    notes_compiling_years = exploration_years * half_factor

    # L2
    book_writing_years = 0.5 # It took .5 years to write his book
    total_time_spent = exploration_years + notes_compiling_years + book_writing_years

    # FA
    answer = total_time_spent
    return answer