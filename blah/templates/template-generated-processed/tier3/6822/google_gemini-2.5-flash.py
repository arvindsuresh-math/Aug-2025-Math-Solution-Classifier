def solve():
    """Index: 6822.
    Returns: the time it would take Meso and Tyler to type 40 pages working together.
    """
    # L1
    meso_pages_typed = 15 # Meso can type 15 pages
    meso_time_taken = 5 # in 5 minutes
    meso_rate = meso_pages_typed / meso_time_taken

    # L2
    tyler_pages_typed = 15 # Tyler can type the same 15 pages
    tyler_time_taken = 3 # in 3 minutes
    tyler_rate = tyler_pages_typed / tyler_time_taken

    # L3
    combined_rate = meso_rate + tyler_rate

    # L4
    target_pages = 40 # type 40 pages
    time_together = target_pages / combined_rate

    # FA
    answer = time_together
    return answer