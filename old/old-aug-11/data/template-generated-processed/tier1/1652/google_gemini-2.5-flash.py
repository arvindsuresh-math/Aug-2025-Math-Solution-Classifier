def solve():
    """Index: 1652.
    Returns: the number of more sheets Jimmy will have than Tommy.
    """
    # L1
    jimmy_sheets_initial = 32 # Jimmy has 32 sheets
    tommy_more_than_jimmy = 10 # Tommy has 10 more sheets than Jimmy does
    tommy_sheets = tommy_more_than_jimmy + jimmy_sheets_initial

    # L2
    ashton_gives_jimmy = 40 # Ashton gives him 40 sheets
    jimmy_sheets_after_ashton = jimmy_sheets_initial + ashton_gives_jimmy

    # L3
    difference_jimmy_vs_tommy = jimmy_sheets_after_ashton - tommy_sheets

    # FA
    answer = difference_jimmy_vs_tommy
    return answer