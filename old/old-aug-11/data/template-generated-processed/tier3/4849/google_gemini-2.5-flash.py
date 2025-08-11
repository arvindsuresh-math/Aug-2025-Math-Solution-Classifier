def solve():
    """Index: 4849.
    Returns: the total length of time it will take to groom the dogs, in minutes.
    """
    # L1
    poodle_groom_time_per_poodle = 30 # It takes 30 minutes to groom a poodle
    num_poodles = 3 # grooms 3 poodles
    total_poodle_groom_time = num_poodles * poodle_groom_time_per_poodle

    # L2
    half_divisor = 2 # half as much time
    terrier_groom_time_per_terrier = poodle_groom_time_per_poodle / half_divisor

    # L3
    num_terriers = 8 # 8 terriers
    total_terrier_groom_time = terrier_groom_time_per_terrier * num_terriers

    # L4
    total_grooming_time = total_poodle_groom_time + total_terrier_groom_time

    # FA
    answer = total_grooming_time
    return answer