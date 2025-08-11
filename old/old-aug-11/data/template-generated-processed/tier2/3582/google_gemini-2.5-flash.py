def solve():
    """Index: 3582.
    Returns: the total cost paid for the camera and lens.
    """
    # L1
    old_camera_cost = 4000 # The old camera cost $4000
    new_model_increase_percent = 0.3 # costs 30% more
    camera_cost_increase = old_camera_cost * new_model_increase_percent

    # L2
    new_camera_cost = old_camera_cost + camera_cost_increase

    # L3
    lens_original_cost = 400 # $400 lens
    lens_discount = 200 # $200 off
    final_lens_cost = lens_original_cost - lens_discount

    # L4
    total_cost = new_camera_cost + final_lens_cost

    # FA
    answer = total_cost
    return answer