def solve():
    """Index: 6347.
    Returns: the total minutes it will take Karen to groom all the dogs.
    """
    # L1
    rottweiler_groom_time = 20 # Rottweilers take 20 minutes to groom
    num_rottweilers = 6 # 6 Rottweilers
    total_time_rottweilers = rottweiler_groom_time * num_rottweilers

    # L2
    border_collie_groom_time = 10 # border collies take 10 minutes to groom
    num_border_collies = 9 # 9 border collies
    total_time_border_collies = border_collie_groom_time * num_border_collies

    # L3
    chihuahua_groom_time = 45 # chihuahuas take 45 minutes to groom
    total_grooming_time = total_time_rottweilers + total_time_border_collies + chihuahua_groom_time

    # FA
    answer = total_grooming_time
    return answer