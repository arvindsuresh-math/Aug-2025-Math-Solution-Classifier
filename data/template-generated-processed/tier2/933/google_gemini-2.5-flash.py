def solve():
    """Index: 933.
    Returns: the total distance climbed in feet.
    """
    # L1
    first_staircase_steps = 20 # The first staircase has 20 steps
    twice_factor = 2 # twice as many steps
    second_staircase_steps = first_staircase_steps * twice_factor

    # L2
    fewer_steps = 10 # 10 fewer steps
    third_staircase_steps = second_staircase_steps - fewer_steps

    # L3
    first_staircase_steps_L3 = 20 # from solution text: 20+40+30
    total_steps = first_staircase_steps_L3 + second_staircase_steps + third_staircase_steps

    # L4
    feet_per_step = 0.5 # Each step is 0.5 feet
    total_feet_climbed = total_steps * feet_per_step

    # FA
    answer = total_feet_climbed
    return answer