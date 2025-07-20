def solve():
    """Index: 6965.
    Returns: the total number of newspapers Julie can print.
    """
    # L1
    packages_per_box = 5 # each containing 5 packages
    sheets_per_package = 250 # 250 sheets of paper per package
    sheets_per_box = packages_per_box * sheets_per_package

    # L2
    num_boxes = 2 # two boxes
    total_sheets = sheets_per_box * num_boxes

    # L3
    sheets_per_newspaper = 25 # uses 25 sheets of paper to print one newspaper
    num_newspapers_printable = total_sheets / sheets_per_newspaper

    # FA
    answer = num_newspapers_printable
    return answer