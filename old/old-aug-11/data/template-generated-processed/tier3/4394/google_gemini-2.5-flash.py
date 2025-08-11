def solve():
    """Index: 4394.
    Returns: the number of craters in Dan's helmet.
    """
    # L1
    rin_craters = 75 # Rin's helmet has 75 craters
    rin_more_than_dan_daniel = 15 # 15 more craters than Dan's and Daniel's helmets combined
    dan_daniel_combined_craters = rin_craters - rin_more_than_dan_daniel

    # L4
    dan_more_than_daniel = 10 # ten more craters
    sum_for_2c = dan_daniel_combined_craters + dan_more_than_daniel

    # L5
    dan_craters = sum_for_2c / 2

    # FA
    answer = dan_craters
    return answer