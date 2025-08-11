def solve():
    """Index: 3233.
    Returns: the average percentage of kernels that pop.
    """
    # L1
    kernels_popped_bag1 = 60 # 60 kernels pop
    total_kernels_bag1 = 75 # bag has 75 kernels
    proportion_bag1 = kernels_popped_bag1 / total_kernels_bag1

    # L2
    kernels_popped_bag2 = 42 # 42 kernels pop
    total_kernels_bag2 = 50 # there are 50 in the bag
    proportion_bag2 = kernels_popped_bag2 / total_kernels_bag2

    # L3
    kernels_popped_bag3 = 82 # 82 kernels pop
    total_kernels_bag3 = 100 # bag has 100 kernels
    proportion_bag3 = kernels_popped_bag3 / total_kernels_bag3

    # L4
    total_proportions = proportion_bag1 + proportion_bag2 + proportion_bag3

    # L5
    num_bags = 3 # WK
    average_proportion = total_proportions / num_bags

    # L6
    percent_multiplier = 100 # WK
    average_percentage = average_proportion * percent_multiplier

    # FA
    answer = average_percentage
    return answer