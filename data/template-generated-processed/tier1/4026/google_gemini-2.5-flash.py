def solve():
    """Index: 4026.
    Returns: the total number of silver dollars the three have.
    """
    # L1
    chiu_dollars = 56 # Mr. Chiu has 56 silver dollars

    # L2
    phung_more_than_chiu = 16 # 16 more silver dollars than Mr. Chiu
    phung_dollars = chiu_dollars + phung_more_than_chiu

    # L3
    ha_more_than_phung = 5 # 5 more silver dollars than Mr. Phung
    ha_dollars = phung_dollars + ha_more_than_phung

    # L4
    total_dollars = ha_dollars + phung_dollars + chiu_dollars

    # FA
    answer = total_dollars
    return answer