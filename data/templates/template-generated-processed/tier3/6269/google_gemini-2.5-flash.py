def solve():
    """Index: 6269.
    Returns: the number of pencils.
    """
    # L1
    total_items = 13 # 13 items
    erasers = 1 # one eraser
    pens_and_pencils = total_items - erasers

    # L2
    # The problem states "The pens are twice as many as the pencils".
    # This means for every 1 pencil part, there are 2 pen parts, totaling 3 parts.
    parts_total = 3 # derived from "twice as many as the pencils"
    pencils = pens_and_pencils / parts_total

    # FA
    answer = pencils
    return answer