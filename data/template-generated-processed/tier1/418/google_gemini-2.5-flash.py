def solve():
    """Index: 418.
    Returns: the number of pencils Ken kept.
    """
    # L1
    pencils_given_to_manny = 10 # Ken gave ten pencils to Manny
    more_pencils_to_nilo = 10 # ten more pencils to Nilo than he gave to Manny
    pencils_received_by_nilo = pencils_given_to_manny + more_pencils_to_nilo

    # L2
    total_given_away = pencils_given_to_manny + pencils_received_by_nilo

    # L3
    initial_pencils = 50 # Ken had fifty pencils
    pencils_kept_by_ken = initial_pencils - total_given_away

    # FA
    answer = pencils_kept_by_ken
    return answer