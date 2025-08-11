def solve():
    """Index: 4146.
    Returns: the number of students who play the alto saxophone.
    """
    # L1
    total_students = 600 # 600 students in the senior class
    marching_band_divisor = 5 # A fifth of the students are in the marching band
    marching_band_students = total_students / marching_band_divisor

    # L2
    brass_instrument_divisor = 2 # half of them play a brass instrument
    brass_instrument_students = marching_band_students / brass_instrument_divisor

    # L3
    saxophone_divisor = 5 # a fifth of them play the saxophone
    saxophone_students = brass_instrument_students / saxophone_divisor

    # L4
    alto_saxophone_divisor = 3 # a third of them play the alto saxophone
    alto_saxophone_students = saxophone_students / alto_saxophone_divisor

    # FA
    answer = alto_saxophone_students
    return answer