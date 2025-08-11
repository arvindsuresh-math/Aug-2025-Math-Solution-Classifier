def solve():
    """Index: 2192.
    Returns: the total amount Suzanne's parents will donate if she finishes the race.
    """
    # L1
    first_km_donation = 10 # $10 for her first kilometer
    multiplier = 2 # double the donation for every successive kilometer
    second_km_donation = first_km_donation * multiplier

    # L2
    third_km_donation = second_km_donation * multiplier

    # L3
    fourth_km_donation = third_km_donation * multiplier

    # L4
    fifth_km_donation = fourth_km_donation * multiplier

    # L5
    total_donation = first_km_donation + second_km_donation + third_km_donation + fourth_km_donation + fifth_km_donation

    # FA
    answer = total_donation
    return answer