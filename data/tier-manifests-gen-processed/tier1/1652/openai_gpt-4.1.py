def solve():
    """Index: 1652.
    Returns: how many more sheets Jimmy has than Tommy after Ashton gives him 40 sheets.
    """
    # L1
    jimmy_sheets = 32 # Jimmy has 32 sheets
    tommy_more_than_jimmy = 10 # Tommy has 10 more sheets than Jimmy
    tommy_sheets = jimmy_sheets + tommy_more_than_jimmy

    # L2
    ashton_gives = 40 # Ashton gives Jimmy 40 sheets
    jimmy_new_sheets = jimmy_sheets + ashton_gives

    # L3
    jimmy_more_than_tommy = jimmy_new_sheets - tommy_sheets

    # FA
    answer = jimmy_more_than_tommy
    return answer