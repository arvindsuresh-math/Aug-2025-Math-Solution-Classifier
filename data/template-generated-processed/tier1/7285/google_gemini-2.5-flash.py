def solve():
    """Index: 7285.
    Returns: the total number of students in the orchestra, the band, and the choir.
    """
    # L1
    orchestra_students = 20 # 20 students in the orchestra
    multiplier_for_band = 2 # twice that number in the band
    band_students = orchestra_students * multiplier_for_band

    # L2
    boys_in_choir = 12 # 12 boys
    girls_in_choir = 16 # 16 girls
    choir_students = boys_in_choir + girls_in_choir

    # L3
    total_students = orchestra_students + band_students + choir_students

    # FA
    answer = total_students
    return answer