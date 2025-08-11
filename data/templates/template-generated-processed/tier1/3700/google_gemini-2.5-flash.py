def solve():
    """Index: 3700.
    Returns: the total number of bottles the three machines can cap in 10 minutes.
    """
    # L1
    machine_a_rate_per_minute = 12 # 12 bottles in 1 minute
    time_in_minutes = 10 # in 10 minutes
    machine_a_total_bottles = machine_a_rate_per_minute * time_in_minutes

    # L2
    machine_b_fewer_than_a = 2 # 2 fewer bottles than Machine A
    machine_b_rate_per_minute = machine_a_rate_per_minute - machine_b_fewer_than_a

    # L3
    machine_b_total_bottles = machine_b_rate_per_minute * time_in_minutes

    # L4
    machine_c_more_than_b = 5 # 5 more bottles than Machine B
    machine_c_rate_per_minute = machine_b_rate_per_minute + machine_c_more_than_b

    # L5
    machine_c_total_bottles = machine_c_rate_per_minute * time_in_minutes

    # L6
    total_bottles_all_machines = machine_a_total_bottles + machine_b_total_bottles + machine_c_total_bottles

    # FA
    answer = total_bottles_all_machines
    return answer