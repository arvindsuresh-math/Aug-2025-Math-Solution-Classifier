def solve():
    """Index: 4397.
    Returns: the total number of goats Max will have.
    """
    # L1
    total_coconuts = 342 # 342 coconuts
    coconuts_per_crab = 3 # 3 coconuts for a crab
    total_crabs = total_coconuts / coconuts_per_crab

    # L2
    crabs_per_goat = 6 # 6 crabs for a goat
    total_goats = total_crabs / crabs_per_goat

    # FA
    answer = total_goats
    return answer