def solve():
    """Index: 5244.
    Returns: the total number of souvenirs Jackson collects.
    """
    # L1
    num_hermit_crabs = 45 # 45 hermit crabs
    shells_per_crab = 3 # 3 spiral shells per hermit crab
    num_spiral_shells = num_hermit_crabs * shells_per_crab

    # L2
    starfish_per_shell = 2 # 2 starfish per spiral shell
    num_starfish = num_spiral_shells * starfish_per_shell

    # L3
    total_souvenirs = num_spiral_shells + num_starfish + num_hermit_crabs

    # FA
    answer = total_souvenirs
    return answer