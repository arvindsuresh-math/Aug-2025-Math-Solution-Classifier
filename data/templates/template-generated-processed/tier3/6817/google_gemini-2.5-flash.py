def solve():
    """Index: 6817.
    Returns: the total cost of the patches for the quilt.
    """
    # L1
    quilt_length = 16 # 16-foot
    quilt_width = 20 # 20-foot
    quilt_area = quilt_length * quilt_width

    # L2
    patch_area = 4 # 4 square feet
    num_patches_needed = quilt_area / patch_area

    # L3
    initial_patches_count = 10 # first 10 patches
    initial_patch_cost = 10 # $10 each
    cost_initial_patches = initial_patches_count * initial_patch_cost

    # L4
    remaining_patches = num_patches_needed - initial_patches_count

    # L5
    discount_divisor = 2 # half as much
    discounted_patch_cost = initial_patch_cost / discount_divisor

    # L6
    cost_discounted_patches = remaining_patches * discounted_patch_cost

    # L7
    total_cost = cost_initial_patches + cost_discounted_patches

    # FA
    answer = total_cost
    return answer