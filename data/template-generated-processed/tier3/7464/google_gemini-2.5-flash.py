def solve():
    """Index: 7464.
    Returns: the total number of kernels Hilary has to shuck.
    """
    # L1
    stalks = 108 # 108 stalks growing
    ears_per_stalk = 4 # four ears of corn per stalk
    total_ears = stalks * ears_per_stalk

    # L2
    kernels_first_half = 500 # 500 kernels of corn
    additional_kernels_second_half = 100 # 100 more
    kernels_second_half = kernels_first_half + additional_kernels_second_half

    # L3
    half_divisor = 2 # Half the ears of corn
    ears_per_half = total_ears / half_divisor

    # L4
    first_half_kernels_total = ears_per_half * kernels_first_half
    second_half_kernels_total = ears_per_half * kernels_second_half
    total_kernels = first_half_kernels_total + second_half_kernels_total

    # FA
    answer = total_kernels
    return answer