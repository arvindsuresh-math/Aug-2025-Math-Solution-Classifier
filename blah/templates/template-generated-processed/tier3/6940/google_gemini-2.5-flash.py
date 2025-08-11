def solve():
    """Index: 6940.
    Returns: the total minutes spent on commercials.
    """
    # L1
    num_programs = 6 # 6 thirty-minute programs
    minutes_per_program = 30 # 6 thirty-minute programs
    total_program_time = num_programs * minutes_per_program

    # L2
    commercial_divisor = 4 # One-fourth of the airing time
    commercial_time = total_program_time / commercial_divisor

    # FA
    answer = commercial_time
    return answer